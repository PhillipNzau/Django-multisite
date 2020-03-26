from django.contrib import admin
from django.urls import path
from django.conf import settings
from blog.views import blog_view
from django.conf.urls.static import static
urlpatterns = [
	path('', blog_view, name='blog'),
	#path('blog/', blog_view),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)