from rest_framework import serializers
from .models import Course, Lesson


class CourseSerializer(serializers.ModelSerializer):
    """Класс описывающий базовый сериалайзер курса"""

    class Meta:
        model = Course
        fields = "__all__"


class LessonSerializer(serializers.ModelSerializer):
    """Класс описывающий базовый сериалайзер урока"""

    class Meta:
        model = Lesson
        fields = "__all__"