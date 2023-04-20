from rest_framework import serializers
from CMS.models import tempCustomer
from RMS.models import RestaurantTable


class tempCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = tempCustomer
        fields = '__all__'


# RMS serializers

class RestaurantTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantTable
        fields = '__all__'
