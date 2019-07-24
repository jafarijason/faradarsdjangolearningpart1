from django.db import models
class Person(models.model):
    first_name = models.CharField(max_lenght  = 30)
    last_name = models.CharField(max_lenght = 30)

class Salam(models.model):
    first_name = models.CharField(max_lenght  = 30)
    last_name = models.CharField(max_lenght = 30)

class Musician (models.model):
    first_name = models.CharField(max_lenght  = 30)
    last_name = models.CharField(max_lenght = 30)
    instrument = models.CharField(max_lenght = 30)

class Album (models.Model):
    artist = models.ForeignKey(Musician,on_delete=models.CASCADE)
    name = models.CharField(max_lenght = 100)
    release_date = models.DateField()
    num_starts = models.IntegerField()


# Create your models here.
