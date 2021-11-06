from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    subtitle = models.TextField()
    author = models.CharField(max_length=50, null=True,blank=True)
    