from django.contrib.gis.db import models

class Shop(models.Model):
    name = models.CharField(max_length=100)
    cost = models.IntegerField(default=10) 
    location = models.PointField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)