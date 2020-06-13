import time
from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to pause execution until database is available"""

    def handle(self, *args, **options):
        self.stdout.write('Waiting for Database')
        dbConn = None
        while not dbConn:
            try:
                dbConn = connections['default']
            except OperationalError:
                self.stdout.write('Database unavailable. Retrying in 1 sec.')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database available.'))
