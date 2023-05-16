from django.db import models

class RestaurantOrderManagementService(models.Model):
    restaurant = models.ForeignKey('Restaurant', on_delete=models.CASCADE)
    orders = models.ManyToManyField('RestaurantOrder')

    def getOrderHistory(self, dateSpan):
        pass

    def getStationaryOrders(self, timeSpan):
        pass

    def getDeliveryOrdersByStatus(self, timeSpan, status):
        pass

    def findBookedTables(self, timeSpan):
        pass

    def findAvailableTables(self, timeSpan, properties):
        pass

    def countAvailableTables(self, timeSpan, properties):
        pass

    def createStationaryOrder(self, booking, customer, menu):
        pass

    def createStationaryOrderBooking(self, booking, customer):
        pass

    def updateStationaryOrder(self, stationaryOrder):
        pass

    def cancelStationaryOrder(self, stationaryOrder):
        pass

    def createDeliveryOrder(self, customer, desiredStartEnd):
        pass

    def updateDeliveryOrder(self, deliveryOrder):
        pass

    def assignAvailableDeliveryWorkerToOrder(self, deliveryOrder):
        pass

    def removeAssignedDeliveryWorkerFromOrder(self, deliveryOrder):
        pass

    def updateDeliveryOrderStatus(self, deliveryOrder, status):
        pass



    def __str__(self):
        return "RestaurantOrderManagementService"
