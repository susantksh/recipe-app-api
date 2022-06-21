"""
Django command to wait for the database to be available
"""
import time

from pyscopg2 import OperationalError as Psycopg2OpError 

from django.db.utils import OperationalError

from django.core.management.base import BaseCommand

class Command(BaseCommand):
    """Django command to wait for database"""

    def handle(self, *args, **options):
        """Entry point for command"""
        self.stdout.write('writing for database')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2OpError, OperationalError):
                self.stdout.write('Database Unavailable, waiting 1 second..')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('database available'))