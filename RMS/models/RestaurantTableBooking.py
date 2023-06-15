from django.db import models
from RMS.models.RestaurantTable import RestaurantTable
from RMS.models.StartEndHours import StartEndHours


class RestaurantTableBooking(models.Model):
    table = models.ForeignKey(RestaurantTable, on_delete=models.CASCADE)
    date = models.DateField()
    startEndHours = models.ForeignKey(StartEndHours, on_delete=models.CASCADE, null=False)
