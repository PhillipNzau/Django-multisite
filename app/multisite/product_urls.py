# blog_urls.py
from django.urls import path, include

urlpatterns = [
    path('', include('product.urls')),
]