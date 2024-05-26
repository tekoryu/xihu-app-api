"""
Django command to wait until database is available.
"""
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to wait for database to be available."""
    def handle(self, *args, **options):
        pass
