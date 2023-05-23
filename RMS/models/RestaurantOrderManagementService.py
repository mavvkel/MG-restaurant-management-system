import StationaryRestaurantOrder
import DeliveryRestaurantOrder
import RestaurantOrder
import RestaurantTableBooking
from django.db import models


class RestaurantOrderManagementService(models.Model):

    def __init__(self, restaurant, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._restaurant = restaurant
        self._orders = []
        self._tables = models.ForeignKey(RestaurantOrder, on_delete=models.CASCADE)

    def get_order_history(self, date_start, date_end):
        order_history = []
        for order in self._orders:
            if date_start <= order.date.date() <= date_end:
                order_history.append(order)
        return

    def get_stationary_orders(self, time_start, time_end):
        stationary_orders = []
        for order in self._orders:
            if order.get_type() == 'stationary' and time_start <= order.date <= time_end:
                stationary_orders.append(order)
        return stationary_orders

    def get_delivery_orders_by_status(self, time_start, time_end, status):
        delivery_orders = []
        for order in self._orders:
            if order.get_type() == 'delivery' and time_start <= order.date <= time_end and order.status == status:
                delivery_orders.append(order)
        return delivery_orders

    # def find_booked_tables(self, time_start, time_end):

    # TO DO: def find_available_tables(self, time_start, time_end, properties):

    # TO DO: def count_booked_tables(self, time_start, time_end, properties):

    # TO DO: all the rest of functions

