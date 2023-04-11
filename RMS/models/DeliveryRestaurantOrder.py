from .Address import Address
import datetime
import StartEndHours
import DeliveryRestaurantOrderStatus
import ContactData
import RestaurantOrder


class DeliveryRestaurantOrder(RestaurantOrder):
    customerAddress = Address
    desiredStartEndHours = StartEndHours
    status = DeliveryRestaurantOrderStatus
    deliveryWorkerId = str
    deliveryWorkerContactData = ContactData


