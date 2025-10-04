from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets, generics, permissions
from django.contrib.auth import get_user_model

from .models import Payment
from .serializers import PaymentSerializer, UserSerializer, RegisterSerializer
from .permissions import IsOwnerOrModeratorWithRestrictions


User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsOwnerOrModeratorWithRestrictions]


class RegisterView(generics.CreateAPIView):
    """Контроллер для регистрации пользователя"""

    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegisterSerializer


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Контроллер для просмотра, изменения и удаления пользователя"""

    queryset = User.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()

class PaymentViewSet(viewsets.ModelViewSet):
    """Класс описывающий вьюсет для платежей с фильтрацией"""

    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ["paid_course", "paid_lesson", "payment_method"]
    ordering_fields = ["payment_date", "amount"]
    ordering = ["-payment_date"]
