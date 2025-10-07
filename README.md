# DjangoRestFramework

API проект для системы управления курсами и уроками, созданный с помощью Django REST Framework.

# Описание
Данный проект реализует API для LMS (Learning Management System), позволяя работать с моделями:

- **Course** — курсы с названием, превью, описанием.
- **Lesson** — уроки, связанные с курсами, с названием, описанием, превью и видео ссылкой.
- **Subscription** - подписка пользователя на курсы.

Реализованы CRUD-операции (создание, чтение, обновление, удаление) для курсов и уроков.

# Особенности
- Python 3.8
- Django 5.2
- Django REST Framework
- django-filter
- djangorestframework-simplejwt
- PostgreSQL
- Testcase
- Использование ViewSet и Generic Views DRF
- Использование сериализаторов
- Использование фильтрации
- Использование JWT авторизации
- Использование валидации, пагинации и тестирование

### Для работы приложения необходимо установить интерпретатор *poetry*:

```pip install --user poetry```

### Так же клонируйте репозиторий:

```git clone https://github.com/Konstantin-Voronin-23/Django_DRF.git```

### Для работы проекта воспользуйтесь командами для установок зависимостей:

```
poetry add --group lint flake8
poetry add --group lint mypy
poetry add --group lint black
poetry add --group lint isort

poetry add --group dev pytest
poetry add coverage
poetry add python-dotenv
pip install psycopg2
poetry add django
poetry add Pillow
poetry add ipython
pip install djangorestframework
poetry add  django-filter
poetry add djangorestframework-simplejwt
```
# Настройка окружения

```
# Настройки Django
SECRET_KEY=ваш-secret-key
DEBUG=True

# База данных PostgreSQL
DB_NAME=mailing
DB_USER=postgres
DB_PASSWORD=ваш-пароль
DB_HOST=localhost
DB_PORT=5432

# Настройки почты (Mail.ru)
EMAIL_HOST_USER=ваш-email@mail.ru
EMAIL_HOST_PASSWORD=пароль-приложения

# Дополнительные настройки
LOCATION=redis://127.0.0.1:6379

```

Применить миграции и создать суперпользователя:

```
python manage.py migrate
python manage.py createsuperuser
```


Запустить сервер разработки:

```
python manage.py runserver
```

# Использование API

### Курсы

- `GET /lms/courses/` - получить список курсов
- `POST /lms/courses/` - создать новый курс
- `GET /lms/courses/<id>/` - получить информацию о курсе
- `PUT /lms/courses/<id>/` - обновить курс
- `DELETE /lms/courses/<id>/` - удалить курс

### Уроки

- `GET /lms/lessons/` - получить список уроков
- `POST /lms/lessons/` - создать новый урок
- `GET /lms/lessons/<id>/` - получить информацию об уроке
- `PUT /lms/lessons/<id>/` - обновить урок
- `DELETE /lms/lessons/<id>/` - удалить урок

# Тестирование

<details>
<summary><b>❗ LessonCRUDTestCase ❗</b></summary>

### test_lesson_list_authenticated:
  - Тест получения списка уроков аутентифицированным пользователем
### test_lesson_list_unauthenticated:
  - Тест получения списка уроков неаутентифицированным пользователем
### test_lesson_create_authenticated:
  - Тест создания урока аутентифицированным пользователем
### test_lesson_create_unauthenticated:
  - Тест создания урока неаутентифицированным пользователем
### test_lesson_retrieve_authenticated:
  - Тест получения деталей урока аутентифицированным пользователем
### test_lesson_update_owner:
  - Тест обновления урока владельцем
### test_lesson_update_not_owner:
  - Тест обновления урока не владельцем
### test_lesson_delete_owner:
  - Тест удаления урока владельцем
### test_lesson_delete_not_owner:
  - Тест удаления урока не владельцем

</details>

<details>
<summary><b>❗ CourseViewSetTestCase ❗</b></summary>

### test_course_list_authenticated:
  - Тест получения списка курсов
### test_course_retrieve_authenticated:
  - Тест получения деталей курса
### test_course_create_authenticated:
  - Тест создания курса

</details>

<details>
<summary><b>❗ SubscriptionTestCase ❗</b></summary>

### test_subscription_create:
  - Тест создания подписки
### test_subscription_delete:
  - Тест удаления подписки
### test_subscription_toggle_unauthenticated:
  - Тест переключения подписки неаутентифицированным пользователем
### test_subscription_toggle_no_course_id:
  - Тест переключения подписки без указания course_id

</details>

# Покрытие тестами 86%

# Лицензия:

Проект распространяется под [лицензией MIT](LICENSE)