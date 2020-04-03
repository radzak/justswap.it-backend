# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand

from ...models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        if not User.objects.filter(username="admin").exists():
            User.objects.create_superuser("admin", "admin@example.com", "admin")
