from django.contrib import admin
from django.urls import path

from product.views import product_view

urlpatterns = [
	path('', product_view, name='product'),
	#path('blog/', blog_view),
]