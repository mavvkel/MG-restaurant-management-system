from rest_framework import serializers
from CMS.models import tempCustomer
from RMS.models import RestaurantTable, Restaurant


class tempCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = tempCustomer
        fields = '__all__'


# RMS serializers

class RestaurantTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantTable
        fields = '__all__'


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'
