"""
Django command to wait until database is available.
"""
import time

from psycopg2 import OperationalError as Psycopg2OpError

from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to wait for database to be available."""
    def handle(self, *args, **options):
        """Entrypoints for command"""
        self.stdout.write('Waiting for database...')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2OpError, OperationalError):
                self.stdout.write(self.style.ERROR('Database not available, waiting for 1 second...'))
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database is available'))