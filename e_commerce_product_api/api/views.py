from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import permissions
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer

# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):
  
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]
  


class CategoryViewSet(viewsets.ModelViewSet):
  
  queryset = Category.objects.all()
  serializer_class = CategorySerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]
