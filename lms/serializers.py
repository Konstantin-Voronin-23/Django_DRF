from rest_framework import serializers

from .models import Course, Lesson
from .validators import validate_youtube


class LessonSerializer(serializers.ModelSerializer):
    """Класс описывающий базовый сериалайзер урока"""

    owner = serializers.PrimaryKeyRelatedField(read_only=True)
    video_url = serializers.URLField(required=False, allow_blank=True, validators=[validate_youtube])

    class Meta:
        model = Lesson
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    """Класс описывающий базовый сериалайзер курса"""

    owner = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Course
        fields = "__all__"


class CourseDetailSerializer(serializers.ModelSerializer):
    """Класс описывающий сериалайзер курса, показывающий количество уроков"""

    lessons_count = serializers.SerializerMethodField()
    lessons = LessonSerializer(many=True, read_only=True)
    owner = serializers.PrimaryKeyRelatedField(read_only=True)
    is_subscribed = serializers.SerializerMethodField()

    def get_lessons_count(self, obj):
        return obj.lessons.count()

    def get_is_subscribed(self, obj):
        user = self.context["request"].user
        if user.is_anonymous:
            return False
        return obj.subscriptions.filter(user=user).exists()

    class Meta:
        model = Course
        fields = "__all__"
