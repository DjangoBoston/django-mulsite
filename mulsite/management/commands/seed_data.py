from django.core.management.base import BaseCommand

# from mulmock import seed

from mulsite import seedmock


class Command(BaseCommand):

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        print('Seeding mock data for Multisite demo')
        seedmock.wipe()
        seedmock.seed_all()
        print('Done.')
