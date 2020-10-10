from django.db import models

# Create your models here.
class Images(models.Model):
    image_link = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=80)
    description = models.TextField()
   
    def __str__(self):
        return self.title

class Categories(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name     

class Locations(models.Model):
    town = models.CharField(max_length=30)
    country = models.CharField(max_length=30)           

    def __str__(self):
        return self.city