from django.db import models
from django.utils.translation import gettext_lazy as _
from RMS.models.RestaurantTableProperty import RestaurantTableProperty


class RestaurantTable(models.Model):
    properties = models.ManyToManyField(RestaurantTableProperty, verbose_name="list of properties")
    capacity = models.PositiveSmallIntegerField(null=False)

    def __str__(self):
        return f'{self.properties.all()} {self.capacity}'

    def add_property(self, table_property: RestaurantTableProperty) -> None:
        self.properties.add(table_property)

    def remove_property(self, table_property: RestaurantTableProperty) -> None:
        self.properties.remove(table_property)
