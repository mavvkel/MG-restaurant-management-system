from rest_framework import serializers
from RMS.models.DishRestaurantMenuEntry import DishRestaurantMenuEntry
from CMS.models import tempCustomer


class tempCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = tempCustomer
        fields = '__all__'


class DishRestaurantMenuEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = DishRestaurantMenuEntry
        fields = ('id', 'name', 'price', 'stage', 'weight')
