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


class RestaurantTable(models.Model):
    properties = models.ManyToManyField(RestaurantTableProperty, verbose_name="list of properties")
    capacity = models.PositiveSmallIntegerField(null=False)

    def __str__(self):
        return f'{self.properties.all()} {self.capacity}'

    def add_property(self, table_property: RestaurantTableProperty) -> None:
        self.properties.add(table_property)

    def remove_property(self, table_property: RestaurantTableProperty) -> None:
        self.properties.remove(table_property)
