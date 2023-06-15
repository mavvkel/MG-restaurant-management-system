from django.db import models


class RestaurantWorkerRole(models.TextChoices):
    WAITER = 'waiter'
    DISHWASHER = 'dishwasher'
    CHEF = 'chef'
    MANAGER = 'manager'
    CLEANER = 'cleaner'
    CUSTOMER_MANAGER = 'customer_manager'
    DELIVERY_MANAGER = 'delivery_manager'
    SYSTEM = 'system'

