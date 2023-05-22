from .Address import Address
import datetime
from RMS.models.StartEndHours import StartEndHours
from RMS.models.ContactData import ContactData
from RMS.models.RestaurantOrder import RestaurantOrder
from django.db import models
from django.utils.translation import gettext_lazy as _


class DeliveryRestaurantOrder(RestaurantOrder):
    class DeliveryRestaurantOrderStatus(models.IntegerChoices):
        CREATED = 1, _('Created')
        IN_PROGRESS = 2, _('In progress')
        AWAITING_ASSIGNMENT = 3, _('Awaiting assignment')
        DELIVERY_IN_PROGRESS = 4, _('Delivery in progress')
        COMPLETED = 5, _('Completed')

    customerAddress = models.ForeignKey(Address, on_delete=models.CASCADE)
    desiredStartEndHours = models.ForeignKey(StartEndHours, on_delete=models.CASCADE)
    status = DeliveryRestaurantOrderStatus
    deliveryWorkerId = models.CharField(max_length=200)
    deliveryWorkerContactData = models.ForeignKey(ContactData, on_delete=models.CASCADE)

    def assign_delivery_worker(self, delivery_id, contact_data):
        self.deliveryWorkerId = delivery_id
        self.deliveryWorkerContactData = contact_data
        self.save()

    @staticmethod
    def get_type():
        return 'delivery'

