===============
E-commerce API
===============

E-commerce API is a Django app designed to manage e-commerce operations such as user authentication, product management, cart functionality, and order processing.

Detailed documentation is in the "docs" directory.

## Quick start

1. Add "api" to your `INSTALLED_APPS` setting like this::

   INSTALLED_APPS = [
   ...,
   "api",
   ]

2. Include the api URLconf in your project's `urls.py` like this::

   from django.urls import path, include

   urlpatterns = [
   ...,
   path("api/", include("api.urls")),
   ]

3. Run `python manage.py migrate` to create the models.

4. Start the development server::

   python manage.py runserver

5. Use an API client like Postman or cURL to test the following endpoints:

   - User Registration: `POST /api/users/register/`
   - User Login: `POST /api/users/login/`
   - Product Management: `GET/POST/PUT/DELETE /api/products/`
   - Cart Management: `GET/POST/DELETE /api/cart/`
   - Order Processing: `GET/POST /api/orders/`

6. Visit the admin panel to manage the database entities::

   http://127.0.0.1:8000/admin/

7. Use the API endpoints to interact with the e-commerce platform as required.

# Authentication Setup

## Description

This project implements JWT-based authentication using Django REST Framework and SimpleJWT.

## Setup Instructions

1. Install the required dependencies:
   pip install djangorestframework
   pip install djangorestframework-simplejwt

2. Update your `settings.py`:

REST_FRAMEWORK = {
'DEFAULT_AUTHENTICATION_CLASSES': (
'rest_framework_simplejwt.authentication.JWTAuthentication',
),
'DEFAULT_PERMISSION_CLASSES': (
'rest_framework.permissions.IsAuthenticated',
),
}
Add the following endpoints to your urls.py:
python
Copier le code
from rest_framework_simplejwt.views import (
TokenObtainPairView,
TokenRefreshView,
)

urlpatterns = [
path('users/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
