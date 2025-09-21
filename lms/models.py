from django.db import models


class Course(models.Model):
    """Класс описывающий модель курса"""

    title = models.CharField(
        max_length=255,
        verbose_name="Название курса",
        help_text="Укажите название курса",
    )

    preview = models.ImageField(
        upload_to="lms/preview_course/",
        verbose_name="Превью",
        help_text="Загрузите превью курса",
        blank=True,
        null=True,
    )

    description = models.TextField(
        verbose_name="Описание курса", help_text="Введите описание курса"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Lesson(models.Model):
    """Класс описывающий модель урока"""

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="lessons",
        verbose_name="Название курса",
        help_text="Укажите название курса",
    )

    title = models.CharField(
        max_length=255,
        verbose_name="Название урока",
        help_text="Укажите название урока",
    )

    description = models.TextField(
        verbose_name="Описание урока", help_text="Введите описание урока"
    )

    preview = models.ImageField(
        upload_to="lms/preview_lesson/",
        verbose_name="Превью",
        help_text="Загрузите превью урока",
        blank=True,
        null=True,
    )

    video_url = models.URLField(
        verbose_name="Ссылка на видео",
        help_text="Укажите ссылку на видеоурок",
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
