from rest_framework.exceptions import ValidationError


def validate_youtube(value):
    """Валидатор для дополнительной проверки на отсутствие в материалах ссылок на сторонние ресурсы,
     кроме youtube.com"""

    if value and "youtube.com" not in value:
        raise ValidationError("Разрешены ссылки только на youtube.com")
    return value
