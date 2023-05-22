from RMS.models.RestaurantTableBooking import RestaurantTableBooking
from RMS.models.RestaurantOrder import RestaurantOrder
from django.db import models


class StationaryRestaurantOrder(RestaurantOrder):
    tableBooking = models.ForeignKey(RestaurantTableBooking, on_delete=models.CASCADE)
    customerComments = models.CharField(max_length=500)

    @staticmethod
    def get_type():
        return 'stationary'
