from typing import List
from django.db import models
from django.utils.translation import gettext_lazy as _
from .RestaurantTableProperty import RestaurantTableProperty


class RestaurantTable(models.Model):

    # TODO: this should be a combination of those choices
    properties = models.ManyToManyField(RestaurantTableProperty, verbose_name="list of properties")
    capacity = models.PositiveSmallIntegerField(null=False)

    def __str__(self):
        return f'{self.properties.all()} {self.capacity}'

    def add_property(self, table_property: RestaurantTableProperty) -> None:
        self.properties.add(table_property)

    def remove_property(self, table_property: RestaurantTableProperty) -> None:
        self.properties.remove(table_property)
