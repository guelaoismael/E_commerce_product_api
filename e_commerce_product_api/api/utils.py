from faker import Faker
from .models import Category, Product

fake = Faker()

def generate_categories(num):
  for _ in range(num):

    name = fake.text(max_nb_chars=8)
    description = fake.text(max_nb_chars=100)

    Category.objects.create(name=name, description=description)

def generate_products(num):
  for _ in range(num):

    name = fake.text(max_nb_chars=10)
    description = fake.text(max_nb_chars=100)
    price = float(fake.random_int(min=85,max=300))
    stock = fake.random_int(min=5, max=80)
    category_id = fake.random_int(min=16, max=20)
    category = Category.objects.get(id=category_id)

    Product.objects.create(name=name, description=description, price = price, stock=stock, category=category)