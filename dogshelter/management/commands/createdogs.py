from django.core.management.base import BaseCommand, CommandError
from dogshelter.models import Dogs

class Command (BaseCommand):
    help = 'Create new strings in Dogs'

    def add_arguments(self, parser):
        parser.add_argument('dog_count', nargs=1, type=int)

    def handle(self, *args, **options):
        dog_count = options['dog_count'][0]

        for i in range(dog_count):
            Dogs.objects.create(id='{0}'.format(i))
        self.stdout.write('Successfully created {0} strings'.format(dog_count))
        