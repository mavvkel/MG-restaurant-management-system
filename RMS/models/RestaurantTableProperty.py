from enum import Enum
from django.db import models
from django.utils.translation import gettext_lazy as _


class RestaurantTableProperty(models.Model):
    NEAR_WINDOW = 1, _('Near window')
    NEAR_KITCHEN = 2, _('Near kitchen')
    IN_GARDEN = 3, _('In garden')
    IN_BAR = 4, _('In bar')
    IS_ISOLATED = 5, _('Is isolated')

    property = models.IntegerField(choices=(
        NEAR_WINDOW,
        NEAR_KITCHEN,
        IN_GARDEN,
        IN_BAR,
        IS_ISOLATED,
    ))

    def __str__(self):
        return str(self.property)
