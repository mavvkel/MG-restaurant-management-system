from django.db import models

# Create your models here.


class tempCustomer(models.Model):
    name = models.CharField(max_length=200)
    create = models.DateTimeField(auto_now_add=True)