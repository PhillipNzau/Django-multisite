from django.db import models

# Create your models here.
class Blog(models.Model):
    title 		= models.TextField(max_length=20)
    description = models.TextField(blank=True, null=True, max_length=120)
    body 		= models.TextField(blank=True, null=True)
    image		= models.ImageField(upload_to='media/', null=True)

