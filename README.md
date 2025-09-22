# DjangoRestFramework

API проект для системы управления курсами и уроками, созданный с помощью Django REST Framework.

# Описание
Данный проект реализует API для LMS (Learning Management System), позволяя работать с моделями:

- **Course** — курсы с названием, превью, описанием.
- **Lesson** — уроки, связанные с курсами, с названием, описанием, превью и видео ссылкой.

Реализованы CRUD-операции (создание, чтение, обновление, удаление) для курсов и уроков.

## Особенности
- Python 3.8
- Django 5.2
- Django REST Framework
- PostgreSQL
- Использование ViewSet и Generic Views DRF

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

poetry add python-dotenv
pip install psycopg2
poetry add django
poetry add Pillow
poetry add ipython
pip install djangorestframework
```
## Настройка окружения

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

## Использование API

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

## Лицензия:

Проект распространяется под [лицензией MIT](LICENSE)