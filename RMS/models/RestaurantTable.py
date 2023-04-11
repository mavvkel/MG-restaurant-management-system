from typing import List
from django.db import models
from .RestaurantTableProperty import RestaurantTableProperty


class RestaurantTable(models.Model):
    capacity = models.PositiveSmallIntegerField
    
    def __init__(self, capacity: int, properties: List[RestaurantTableProperty], *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.properties = properties

    def add_property(self, table_property: RestaurantTableProperty) -> None:
        self.properties.append(table_property)

    def remove_property(self, table_property: RestaurantTableProperty) -> None:
        self.properties.remove(table_property)
