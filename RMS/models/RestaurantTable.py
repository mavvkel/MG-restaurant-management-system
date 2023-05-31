from typing import List
from django.db import models
from django.utils.translation import gettext_lazy as _
from .RestaurantTableProperty import RestaurantTableProperty


class RestaurantTable(models.Model):
    class RestaurantTableProperty(models.IntegerChoices):
        NEAR_WINDOW = 1, _('Near window')
        NEAR_KITCHEN = 2, _('Near kitchen')
        IN_GARDEN = 3, _('In garden')
        IN_BAR = 4, _('In bar')
        IS_ISOLATED = 5, _('Is isolated')

    properties = models.IntegerField(choices=RestaurantTableProperty.choices)
    capacity = models.PositiveSmallIntegerField(null=False)

    def __str__(self):
        return f'{self.properties} {self.capacity}'
        # if self.properties == 1:
        #     return f'Near window {self.capacity}'
        # elif self.properties == 2:
        #     return f'Near kitchen {self.capacity}'
        # elif self.properties == 3:
        #     return f'In garden {self.capacity}'
        # elif self.properties == 4:
        #     return f'In bar {self.capacity}'
        # elif self.properties == 5:
        #     return f'Is isolated {self.capacity}'
        # else:
        #     return f'None {self.capacity}'

    def add_property(self, table_property: RestaurantTableProperty) -> None:
        self.properties.append(table_property)

    def remove_property(self, table_property: RestaurantTableProperty) -> None:
        self.properties.remove(table_property)
