from .Address import Address
import datetime
import StartEndHours
import DeliveryRestaurantOrderStatus
import ContactData


class DeliveryRestaurantOrder:
    customerAddress = Address
    date = datetime
    desiredStartEndHours = StartEndHours
    status = DeliveryRestaurantOrderStatus
    deliveryWorkerId = str
    deliveryWorkerContactData = ContactData


