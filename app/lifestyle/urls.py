from django.contrib import admin
from django.urls import path

from lifestyle.views import lifestyle_view

urlpatterns = [
	path('', lifestyle_view, name='lifestyle'),
	#path('blog/', blog_view),
]