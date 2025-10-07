from django.urls import include, path
from rest_framework.routers import DefaultRouter

from lms.apps import LmsConfig

from .views import (CourseViewSet, LessonListCreateAPIView, LessonRetrieveUpdateDestroyAPIView,
                    SubscriptionToggleAPIView)

app_name = LmsConfig.name

router = DefaultRouter()
router.register(r"courses", CourseViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("lessons/", LessonListCreateAPIView.as_view(), name="lesson-list-create"),
    path(
        "lessons/<int:pk>/",
        LessonRetrieveUpdateDestroyAPIView.as_view(),
        name="lesson-detail",
    ),
    path(
        "subscriptions/toggle/",
        SubscriptionToggleAPIView.as_view(),
        name="subscription-toggle",
    ),
]

urlpatterns += router.urls
