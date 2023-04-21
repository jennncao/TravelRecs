from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class State(models.Model):
    name = models.CharField(max_length = 255)

    class Meta:
        verbose_name_plural = 'states'

    def __str__(self):
        return self.name

#attempt at category subclass to use with activity class for filtering reasons 
'''class Category(models.Model):
    name = models.CharField(max_length = 100, null = True)

    def __str__(self):
        return self.name'''

class Activity(models.Model):
    '''def __init__(self):
            self.category = Category()'''

    state = models.CharField(max_length = 20, null = True)
    abv = models.CharField(max_length = 3, null = True)
    name = models.CharField(max_length = 100, null = True)
    category = models.CharField(max_length = 100, null = True) 
    image = models.CharField(max_length = 300, null = True)
    link = models.CharField(max_length = 200, null = True)
    description = models.CharField(max_length = 400, null = True)
    address = models.CharField(max_length = 100, null = True)
    favorite = models.ManyToManyField(User, related_name = 'activities')
    objects = models.Manager() #default 

    def __str__(self):
        return self.name
    
    objects = models.Manager()