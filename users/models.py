from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Класс описывающий модель пользователя"""

    username = None

    email = models.EmailField(unique=True, verbose_name="Почта", help_text="Введите email")

    phone = models.CharField(
        max_length=35, blank=True, null=True, verbose_name="Телефон", help_text="Укажите номер телефона"
    )

    sity = models.CharField(max_length=50, blank=True, null=True, verbose_name="Город", help_text="Укажите ваш город")

    avatar = models.ImageField(
        upload_to="users/avatars", blank=True, null=True, verbose_name="Аватар", help_text="Загружите ваш аватар"
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

class Meta:
    verbose_name = 'Пользователь'
    verbose_name_plural = 'Пользователи'
