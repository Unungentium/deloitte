from django.core.management.base import BaseCommand, CommandError
from bigc.models import CompanyName as Company
from django.db import IntegrityError
class Command(BaseCommand):
    help = 'creates a company with a name'
    def add_arguments(self, parser):
        parser.add_argument('names', nargs='+', type=str)
    def handle(self, *args, **kwargs):
        for CompanyName in kwargs['names']:
            try:
                Company.objects.create(name=CompanyName)
            except IntegrityError:
                print("cannot create duplicates")
        
