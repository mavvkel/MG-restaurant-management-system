from django.db import models
from django.core.validators import MinLengthValidator
from django.core.validators import MinValueValidator


class RestaurantMenuEntry(models.Model):

    class Meta:
        abstract = True

    name = models.CharField(max_length=200,
                            validators=[MinLengthValidator(limit_value=2,
                                                           message='Name must be at least 2 characters long.')])
    price = models.DecimalField(max_digits=19,
                                decimal_places=2,
                                validators=[MinValueValidator(limit_value=0,
                                                              message='Price cannot be negative.')])

    def __str__(self):
        return self.name
