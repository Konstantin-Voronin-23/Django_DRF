from django.conf import settings
from django.contrib.auth.models import Group
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Создает группу пользователей"

    def handle(self, *args, **kwargs):
        groups = [settings.MODERATOR_GROUP_NAME]
        for group_name in groups:
            group, created = Group.objects.get_or_create(name=group_name)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Группа {group_name} успешно создана"))
            else:
                self.stdout.write(f"Группа {group_name} уже существует")
