from django.db import models


class Address(models.Model):
    street = models.CharField(max_length=200)
    house = models.CharField(max_length=20)
    section = models.CharField(max_length=200) 
    flat = models.CharField(max_length=20) 

