from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=55)
    subtitle = models.CharField(max_length=120)
    text = models.TextField()
