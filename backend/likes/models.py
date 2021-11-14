from django.db import models

# Create your models here.

class Likes(models.Model):
    name = models.CharField(max_length=256)
    uploader = models.CharField(max_length=256)
    thumbnail = models.URLField(max_length=256)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
    
   
