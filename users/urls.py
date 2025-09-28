from django.urls import include, path
from users.apps import UsersConfig
from rest_framework.routers import DefaultRouter

from .views import PaymentViewSet, UserDetailView, RegisterView
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r"payments", PaymentViewSet, basename="payment")

app_name = UsersConfig.name

urlpatterns = [
    path("", include(router.urls)),
    path("register/", RegisterView.as_view(), name="register"),
    path("login/",TokenObtainPairView.as_view(permission_classes=(AllowAny,)), name="login"),
    path("token/refresh/", TokenRefreshView.as_view(permission_classes=(AllowAny,)), name="token_refresh"),
    path("user/", UserDetailView.as_view(), name="user_detail"),
]
