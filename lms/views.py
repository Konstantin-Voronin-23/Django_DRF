from rest_framework import viewsets, generics
from .models import Course, Lesson
from .serializers import CourseSerializer, LessonSerializer


class CourseViewSet(viewsets.ModelViewSet):
    """ViewSet для работы с курсами.
    Предоставляет полный CRUD (создание, чтение, обновление, удаление)
    для модели Course через стандартные HTTP-методы.
    Автоматически генерирует все необходимые эндпоинты для работы с курсами"""

    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class LessonListCreateAPIView(generics.ListCreateAPIView):
    """API для получения списка уроков и создания нового урока.
    GET-запрос возвращает список всех уроков.
    POST-запрос создает новый урок с переданными данными"""

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """API для работы с конкретным уроком. Предоставляет операции:
    - GET: получение данных конкретного урока
    - PUT: полное обновление урока
    - PATCH: частичное обновление урока
    - DELETE: удаление урока"""

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
