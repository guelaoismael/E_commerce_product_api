from django.db import models

# Create your models here.
class Category(models.Model):
  
  name = models.CharField(max_length=150)
  description = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.name

class Product(models.Model):
  
  name = models.CharField(max_length=150)
  description = models.TextField()
  price = models.FloatField()
  stock = models.PositiveIntegerField()
  category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.name