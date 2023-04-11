from django.db import models
from .RestaurantMenuEntry import RestaurantMenuEntry
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator


class DishRestaurantMenuEntry(RestaurantMenuEntry):

    class DishStage(models.IntegerChoices):
        STARTER = 1, _('Starter')
        MAIN_COURSE = 2, _('Main course')
        SOUP = 3, _('Soup')
        SALAD = 4, _('Salad')
        DESSERT = 5, _('Dessert')

    stage = models.IntegerField(choices=DishStage.choices)
    weight = models.DecimalField(max_digits=19,
                                 decimal_places=3,
                                 validators=[MinValueValidator(limit_value=0.0,
                                                               message='Weight cannot be negative.')])
