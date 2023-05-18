from rest_framework import serializers
from RMS.models.DishRestaurantMenuEntry import DishRestaurantMenuEntry
from CMS.models import tempCustomer
from RMS.models.RestaurantWorker import RestaurantWorker
from RMS.models.Restaurant import Restaurant
from RMS.models.DeliveryRestaurantOrder import DeliveryRestaurantOrder
from RMS.models.StationaryRestaurantOrder import StationaryRestaurantOrder


class tempCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = tempCustomer
        fields = '__all__'


class DishRestaurantMenuEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = DishRestaurantMenuEntry
        fields = ('id', 'name', 'price', 'stage', 'weight')


class RestaurantWorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantWorker
        fields = ('id', 'name', 'role', 'availability')


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'


class RestaurantTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('_menu', '_workers', '_tables', '_availability')


class DeliveryRestaurantOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryRestaurantOrder
        fields = ('customerAddress', 'desiredStartEndHours', 'status', 'deliveryWorkerContactData', 'date',
                  'menu_selection')


class StationaryRestaurantOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = StationaryRestaurantOrder
        fields = ('tableBooking', 'customerComments', 'date', 'menu_selection')
