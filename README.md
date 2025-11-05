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
- drf_spectacular
- PostgreSQL
- Testcase
- Docker
- Использование ViewSet и Generic Views DRF
- Использование сериализаторов
- Использование фильтрации
- Использование JWT авторизации
- Использование валидации, пагинации и тестирование
- Использование автодокументации (spectacular) и интеграция API (STRIPE)
- Docker Compose
- Nginx 
- CI/CD
- GitHub Actions

# Зависимости (requirements.txt)

```
Django==5.2.6
djangorestframework==3.16.1
django-filter==25.1
djangorestframework_simplejwt==5.5.1
django-extensions==4.1
drf-spectacular==0.29.0
django-celery-beat==2.8.1
celery==5.3.6
eventlet==0.34.1
python-dotenv==1.1.1
psycopg2-binary==2.9.10
pillow==11.3.0
redis==5.0.3
black==25.1.0
pytest-django==4.11.1
coverage==7.10.7
stripe==13.0.1
```
# Настройка окружения

```
# Настройки Django
SECRET_KEY=ваш-secret-key
DEBUG=True

# База данных PostgreSQL
DB_NAME=lms
DB_USER=postgres
DB_PASSWORD=ваш-пароль
DB_HOST=db
DB_PORT=5432

# Настройки почты (Mail.ru)
EMAIL_HOST_USER=ваш-email@mail.ru
EMAIL_HOST_PASSWORD=пароль-приложения

# Дополнительные настройки
LOCATION=redis://redis:6379/0

# Настройки интеграции STRIPE.com
STRIPE_SECRET_KEY=ваш API SECRET_KEY
STRIPE_PUBLISHABLE_KEY=ваш API PUBLISHABLE_KEY
```

# Использование API

##  Быстрый старт (Docker Compose)

1. Клонировать репозиторий:
~~~
git clone https://github.com/Konstantin-Voronin-23/Django_DRF.git
cd Django_DRF
~~~

2. Заполните переменные окружения:
~~~
cp .env.example .env
nano .env
~~~
* Скопируйте .env.sample и пропишите конфиг доступа к БД, Redis, секретные ключи.

3. Запустить проект одной командой:

~~~
docker-compose up --build
~~~

4. Готово!

* Откройте http://localhost:8000 и пользуйтесь API.

<details>
<summary><b>❗ Проверка сервисов и диагностика ❗</b></summary>

### Celery Worker:
  - docker-compose logs celery_worker
  - celery@... ready. Connected to redis://redis:6379/0
### Celery Beat:
  - docker-compose logs celery_beat
  - beat: Starting... DatabaseScheduler: Schedule changed
### PostgreSQL:
  - Войти внутрь контейнера
  - docker exec -it lms psql -U postgres -d lms
  - Проверить пользователей
  - SELECT id, username, email, last_login, is_active FROM auth_user;

</details>

## Курсы

- `GET /lms/courses/` - получить список курсов
- `POST /lms/courses/` - создать новый курс
- `GET /lms/courses/<id>/` - получить информацию о курсе
- `PUT /lms/courses/<id>/` - обновить курс
- `DELETE /lms/courses/<id>/` - удалить курс

## Уроки

- `GET /lms/lessons/` - получить список уроков
- `POST /lms/lessons/` - создать новый урок
- `GET /lms/lessons/<id>/` - получить информацию об уроке
- `PUT /lms/lessons/<id>/` - обновить урок
- `DELETE /lms/lessons/<id>/` - удалить урок

# Тестирование

Как запускать тесты?
~~~
docker compose run web pytest
~~~
Все основные компоненты покрыты unit и интеграционными тестами.

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

# Настройка удалённого сервера

1. Установите необходимые пакеты на сервере:

~~~
sudo apt update
sudo apt install python3 python3-pip python3-venv nginx docker docker-compose git
~~~

2. Настройте SSH-доступ с помощью ключей для безопасного подключения, закройте все ненужные порты с помощью firewall.

3. Подготовьте проект:

* Клонируйте репозиторий на сервер:

~~~
git clone https://github.com/Konstantin-Voronin-23/Django_DRF.git
cd Django_DRF
~~~

* Создайте и заполните .env файл скопировав шаблон:

~~~
cp .env.sample .env
nano .env
~~~

4. Запустите миграции и сборку статики (при необходимости):

~~~
docker compose run web python manage.py migrate
docker compose run web python manage.py collectstatic --noinput
~~~

5. Запустите приложение в Docker:

~~~
docker compose up -d --build
~~~

# Автоматизация деплоя через GitHub Actions
1. В репозитории создайте файл workflow в .github/workflows/ci-cd.yml.

2. Конфигурируйте workflow для запуска тестов и деплоя (пример ниже):

```
name: CI/CD Pipeline

on: push

jobs:
  test:
    runs-on: ubuntu-latest

    services:
      postgres:
        image: postgres:15
        env:
          POSTGRES_DB: test_db
          POSTGRES_USER: postgres
          POSTGRES_PASSWORD: postgres
        options: >-
          --health-cmd pg_isready
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5
        ports:
          - 5432:5432

    env:
      SECRET_KEY: ${{ secrets.SECRET_KEY }}
      DEBUG: "True"
      DB_ENGINE: "django.db.backends.postgresql"
      DB_NAME: "test_db"
      DB_USER: "postgres"
      DB_PASSWORD: "postgres"
      DB_HOST: "localhost"
      DB_PORT: "5432"

    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: "3.12"

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Run migrations
        run: |
          python manage.py migrate

      - name: Run tests
        run: |
          python manage.py test

  deploy:
    needs: test
    if: success()
    runs-on: ubuntu-latest
    steps:
      - name: Deploy to server via SSH
        uses: appleboy/ssh-action@v0.1.7
        with:
          host: ${{ secrets.SERVER_HOST }}
          username: ${{ secrets.SERVER_USER }}
          key: ${{ secrets.SERVER_SSH_KEY }}
          port: ${{ secrets.SERVER_PORT }}
          script: |
            cd ~/Django_DRF/Django_DRF
            git pull origin main
            docker compose down
            docker compose pull
            docker compose up -d --build

```

3. Добавьте необходимые секреты в GitHub Secrets:

SERVER_HOST, SERVER_USER, SERVER_SSH_KEY, SERVER_PORT, SECRET_KEY

4. Проверка результатов
После пуша в репозиторий тесты выполняются автоматически.

При успешных тестах проект деплоится на сервер.

При ошибках в тестах деплой не происходит.

# Логирование и мониторинг
* Логи приложения доступны через

~~~
docker compose logs web
~~~

* Gunicorn логирует события старта, ошибок и работы воркеров.

* Nginx логирует HTTP-запросы и ошибки, логи доступны через

~~~
docker compose logs nginx
~~~

* Для продакшена рекомендуется настроить внешние системы логирования и мониторинга (Prometheus, ELK стек или другое)

# Покрытие тестами 86%

# Лицензия:

Проект распространяется под [лицензией MIT](LICENSE)