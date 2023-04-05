from enum import Enum


class DeliveryRestaurantOrderStatus(Enum):
    CREATED = 1
    IN_PROGRESS = 2
    AWAITING_ASSIGNMENT = 3
    DELIVERY_IN_PROGRESS = 4
    COMPLETED = 5
