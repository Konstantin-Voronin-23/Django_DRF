from django.urls import include, path
from users.apps import UsersConfig
from rest_framework.routers import DefaultRouter

from .views import PaymentViewSet

router = DefaultRouter()
router.register(r"payments", PaymentViewSet, basename="payment")

app_name = UsersConfig.name

urlpatterns = [
    path("", include(router.urls)),
]
