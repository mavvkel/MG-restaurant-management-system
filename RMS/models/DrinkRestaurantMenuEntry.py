from django.db import models
from .RestaurantMenuEntry import RestaurantMenuEntry
from django.core.validators import MinValueValidator


class DrinkRestaurantMenuEntry(RestaurantMenuEntry):
    contains_alcohol = models.BooleanField(verbose_name='Contains alcohol',
                                           default=False)
    volume = models.DecimalField(max_digits=19,
                                 decimal_places=4,
                                 validators=[MinValueValidator(limit_value=0.0,
                                                               message='Volume cannot be negative.')])
