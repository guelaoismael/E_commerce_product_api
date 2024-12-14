from django.core.management.base import BaseCommand

from ...utils import generate_categories, generate_products

class Command(BaseCommand):
  
  def handle(self, *args, **options):
   generate_categories(5)
   generate_products(10)