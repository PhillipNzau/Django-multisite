from django.contrib import admin
from django.urls import path

from sports.views import sports_view

urlpatterns = [
	path('', sports_view, name='sports'),
	#path('blog/', blog_view),
]