from django.db import models
import RestaurantTable
import StartEndHours


class RestaurantTableBooking(models.Model):
    table = models.ForeignKey(RestaurantTable, on_delete=models.CASCADE)
    date = models.DateTimeField()
    startEndHours = models.ForeignKey(StartEndHours, on_delete=models.CASCADE)
