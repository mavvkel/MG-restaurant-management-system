from typing import List
from enum import Enum
from RestaurantTableProperty import RestaurantTableProperty



class RestaurantTable:
    def __init__(self, capacity: int, properties: List[RestaurantTableProperty]):
        self.capacity = capacity
        self.properties = properties

    def addProperty(self, property: RestaurantTableProperty) -> None:
        self.properties.append(property)

    def removeProperty(self, property: RestaurantTableProperty) -> None:
        self.properties.remove(property)
