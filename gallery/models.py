from django.db import models

# Create your models here.
class Images(models.Model):
    image_link = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=80)
    description = models.TextField()
    category = models.ForeignKey('Categories', on_delete=models.CASCADE, default=1)
    location = models.ForeignKey('Locations', on_delete=models.CASCADE, default=1)
   
    def __str__(self):
        return self.title

    @classmethod
    def get_all(cls):
        pics = Images.objects.all()
        return pics   

    @classmethod
    def search_image(cls, cat):
        '''
        method to search images by category
        '''
        retrieved = cls.objects.filter(category__name__contains=cat) #images assoc w/ this cat
        return retrieved #list of instances
    
    @classmethod
    def filter_by_location(cls ,location):
        '''
        method to retrive images by their locations
        '''
        retrieved = Images.objects.filter(location__town__contains=location)
        return retrieved

class Categories(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name     

class Locations(models.Model):
    town = models.CharField(max_length=30)
    country = models.CharField(max_length=30)           

    def __str__(self):
        return self.town

    @classmethod
    def get_all(cls):
        '''
        method to retrive all stored locations
        '''
        cities = Locations.objects.all()
        return cities    