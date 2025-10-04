from rest_framework import viewsets, generics, permissions
from .models import Course, Lesson
from .serializers import CourseSerializer, LessonSerializer
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsModerator, IsOwner
from django.conf import settings


class CourseViewSet(viewsets.ModelViewSet):
    """ViewSet для работы с курсами.
    Предоставляет полный CRUD (создание, чтение, обновление, удаление)
    для модели Course через стандартные HTTP-методы.
    Автоматически генерирует все необходимые эндпоинты для работы с курсами"""

    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    moderator_group = settings.MODERATOR_GROUP_NAME

    def get_permissions(self):
        read_actions  = ['list', 'retrieve', 'update', 'partial_update']

        if self.action == 'create':
            permission_classes = [permissions.IsAuthenticated, ~IsModerator]
        elif self.action == 'destroy':
            permission_classes = [permissions.IsAuthenticated, IsOwner]
        elif self.action in read_actions:
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [permissions.IsAuthenticated]

        return [perm() for perm in permission_classes]

    def get_queryset(self):
        user = self.request.user
        if user.groups.filter(name=self.moderator_group).exists():
            return Course.objects.all()
        return Course.objects.filter(owner=user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LessonListCreateAPIView(generics.ListCreateAPIView):
    """API для получения списка уроков и создания нового урока.
    GET-запрос возвращает список всех уроков.
    POST-запрос создает новый урок с переданными данными"""

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

    moderator_group = settings.MODERATOR_GROUP_NAME

    def get_permissions(self):
        if self.request.method == "POST":
            if self._is_moderator():
                self.permission_denied(
                    self.request,
                    message="Модераторам запрещено создавать уроки"
                )

        permission_classes = [permissions.IsAuthenticated]
        return [perm() for perm in permission_classes]

    def get_queryset(self):
        if self._is_moderator():
            return Lesson.objects.all()
        return Lesson.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def _is_moderator(self):
        return self.request.user.groups.filter(name=self.moderator_group).exists()


class LessonRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """API для работы с конкретным уроком. Предоставляет операции:
    - GET: получение данных конкретного урока
    - PUT: полное обновление урока
    - PATCH: частичное обновление урока
    - DELETE: удаление урока"""

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

    moderator_group = settings.MODERATOR_GROUP_NAME

    read_update_methods = ["GET", "PUT", "PATCH"]

    def get_permissions(self):
        if self.request.method == "DELETE":
            permission_classes = [permissions.IsAuthenticated, IsOwner]
        elif self.request.method in self.read_update_methods:
            permission_classes = [permissions.IsAuthenticated, IsOwner]
        else:
            permission_classes = [permissions.IsAuthenticated]

        return [perm() for perm in permission_classes]

    def get_object(self):
        obj = super().get_object()

        if self._is_moderator():
            return obj

        self.check_object_permissions(self.request, obj)
        return obj

    def _is_moderator(self):
        return self.request.user.groups.filter(name=self.moderator_group).exists()
