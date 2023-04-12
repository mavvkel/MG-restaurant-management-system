from django.db import models
from django.utils.translation import gettext_lazy as _

class RestaurantWorkerRole(models.IntegerChoices):
    WAITER = 1, _('Waiter')
    DISHWASHER = 2, _('Dishwasher')
    CHEF = 3, _('Chef')
    MANAGER = 4, _('Manager')
    CLEANER = 5, _('Cleaner')