from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from lms.models import Course, Lesson, Subscription

User = get_user_model()


class LessonCRUDTestCase(APITestCase):
    """Тесты для CRUD операций с уроками"""

    def setUp(self):
        """Настройка тестовых данных"""

        # Создаем пользователей
        self.owner = User.objects.create_user(email="owner@test.com", password="testpass123")
        self.moderator = User.objects.create_user(email="moderator@test.com", password="testpass123")
        self.other_user = User.objects.create_user(email="other@test.com", password="testpass123")

        # Создаем курс
        self.course = Course.objects.create(title="Test Course", description="Test Description", owner=self.owner)

        # Создаем урок
        self.lesson = Lesson.objects.create(
            course=self.course, title="Test Lesson", description="Test Lesson Description", owner=self.owner
        )

        # URL для уроков
        self.lessons_list_url = reverse("lms:lesson-list-create")
        self.lesson_detail_url = reverse("lms:lesson-detail", kwargs={"pk": self.lesson.pk})

    def test_lesson_list_authenticated(self):
        """Тест получения списка уроков аутентифицированным пользователем"""

        self.client.force_authenticate(user=self.owner)
        response = self.client.get(self.lessons_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_lesson_list_unauthenticated(self):
        """Тест получения списка уроков неаутентифицированным пользователем"""

        response = self.client.get(self.lessons_list_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_lesson_create_authenticated(self):
        """Тест создания урока аутентифицированным пользователем"""

        self.client.force_authenticate(user=self.owner)

        data = {
            "course": self.course.id,
            "title": "New Lesson",
            "description": "New Lesson Description",
        }

        response = self.client.post(self.lessons_list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Lesson.objects.count(), 2)
        self.assertEqual(Lesson.objects.last().owner, self.owner)

    def test_lesson_create_unauthenticated(self):
        """Тест создания урока неаутентифицированным пользователем"""

        data = {
            "course": self.course.id,
            "title": "New Lesson",
            "description": "New Lesson Description",
        }

        response = self.client.post(self.lessons_list_url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_lesson_retrieve_authenticated(self):
        """Тест получения деталей урока аутентифицированным пользователем"""

        self.client.force_authenticate(user=self.owner)
        response = self.client.get(self.lesson_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.lesson.title)

    def test_lesson_update_owner(self):
        """Тест обновления урока владельцем"""

        self.client.force_authenticate(user=self.owner)

        data = {"title": "Updated Lesson Title", "description": self.lesson.description, "course": self.course.id}

        response = self.client.put(self.lesson_detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.lesson.refresh_from_db()
        self.assertEqual(self.lesson.title, "Updated Lesson Title")

    def test_lesson_update_not_owner(self):
        """Тест обновления урока не владельцем"""

        self.client.force_authenticate(user=self.other_user)

        data = {"title": "Updated Lesson Title", "description": self.lesson.description, "course": self.course.id}

        response = self.client.put(self.lesson_detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_lesson_delete_owner(self):
        """Тест удаления урока владельцем"""

        self.client.force_authenticate(user=self.owner)
        response = self.client.delete(self.lesson_detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Lesson.objects.count(), 0)

    def test_lesson_delete_not_owner(self):
        """Тест удаления урока не владельцем"""

        self.client.force_authenticate(user=self.other_user)
        response = self.client.delete(self.lesson_detail_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Lesson.objects.count(), 1)


class SubscriptionTestCase(APITestCase):
    """Тесты для функционала подписки на курс"""

    def setUp(self):
        """Настройка тестовых данных"""

        # Создаем пользователя
        self.user = User.objects.create_user(email="user@test.com", password="testpass123")

        # Создаем курс
        self.course = Course.objects.create(title="Test Course", description="Test Description", owner=self.user)

        # URL для подписок
        self.subscription_toggle_url = reverse("lms:subscription-toggle")

    def test_subscription_create(self):
        """Тест создания подписки"""

        self.client.force_authenticate(user=self.user)

        data = {"course_id": self.course.id}

        response = self.client.post(self.subscription_toggle_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["message"], "подписка добавлена")
        self.assertTrue(Subscription.objects.filter(user=self.user, course=self.course).exists())

    def test_subscription_delete(self):
        """Тест удаления подписки"""

        # Сначала создаем подписку
        Subscription.objects.create(user=self.user, course=self.course)

        self.client.force_authenticate(user=self.user)

        data = {"course_id": self.course.id}

        response = self.client.post(self.subscription_toggle_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["message"], "подписка удалена")
        self.assertFalse(Subscription.objects.filter(user=self.user, course=self.course).exists())

    def test_subscription_toggle_unauthenticated(self):
        """Тест переключения подписки неаутентифицированным пользователем"""

        data = {"course_id": self.course.id}

        response = self.client.post(self.subscription_toggle_url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_subscription_toggle_no_course_id(self):
        """Тест переключения подписки без указания course_id"""

        self.client.force_authenticate(user=self.user)

        data = {}

        response = self.client.post(self.subscription_toggle_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("error", response.data)


class CourseViewSetTestCase(APITestCase):
    """Тесты для ViewSet курсов"""

    def setUp(self):
        """Настройка тестовых данных"""

        self.owner = User.objects.create_user(email="owner@test.com", password="testpass123")
        self.other_user = User.objects.create_user(email="other@test.com", password="testpass123")

        self.course = Course.objects.create(title="Test Course", description="Test Description", owner=self.owner)

        # Создаем несколько уроков для курса
        self.lesson1 = Lesson.objects.create(
            course=self.course, title="Lesson 1", description="Description 1", owner=self.owner
        )
        self.lesson2 = Lesson.objects.create(
            course=self.course, title="Lesson 2", description="Description 2", owner=self.owner
        )

    def test_course_list_authenticated(self):
        """Тест получения списка курсов"""

        self.client.force_authenticate(user=self.owner)
        url = reverse("lms:course-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_course_retrieve_authenticated(self):
        """Тест получения деталей курса"""

        self.client.force_authenticate(user=self.owner)
        url = reverse("lms:course-detail", kwargs={"pk": self.course.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.course.title)

    def test_course_create_authenticated(self):
        """Тест создания курса"""

        self.client.force_authenticate(user=self.owner)
        url = reverse("lms:course-list")

        data = {
            "title": "New Course",
            "description": "New Course Description",
        }

        response = self.client.post(url, data)

        print("=== DEBUG COURSE CREATE ===")
        print(f"Status code: {response.status_code}")
        print(f"Response data: {response.data}")
        print("===========================")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Course.objects.count(), 2)
        self.assertEqual(Course.objects.last().owner, self.owner)
