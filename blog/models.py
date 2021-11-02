from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    Author = models.CharField(max_length=20)

    def __str__(self):
        return "{}".format(self.title)