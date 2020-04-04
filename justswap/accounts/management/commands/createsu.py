# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand

from justswap.accounts.models import User


class Command(BaseCommand):
    """Django create super user management command."""

    def handle(self, *args, **options) -> None:  # noqa: WPS110
        """The actual logic of the command."""
        if not User.objects.filter(username="admin").exists():
            User.objects.create_superuser("admin", "admin@example.com", "admin")
