from django.db import models
from django.utils.translation import gettext_lazy as _


class DeliveryRestaurantOrderStatus(models.IntegerChoices):
    CREATED = 1, _('Created')
    IN_PROGRESS = 2, _('In progress')
    AWAITING_ASSIGNMENT = 3, _('Awaiting assignment')
    DELIVERY_IN_PROGRESS = 4, _('Delivery in progress')
    COMPLETED = 5, _('Completed')
