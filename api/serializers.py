from rest_framework import serializers
from RMS.models.RestaurantMenuEntry import RestaurantMenuEntry
from RMS.models.DishRestaurantMenuEntry import DishRestaurantMenuEntry
from RMS.models.DrinkRestaurantMenuEntry import DrinkRestaurantMenuEntry
from RMS.models.RestaurantTable import RestaurantTable, RestaurantTableProperty
from RMS.models.RestaurantWorker import *
from CMS.models import tempCustomer
from rest_polymorphic.serializers import PolymorphicSerializer


class tempCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = tempCustomer
        fields = '__all__'


class RestaurantAvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantAvailability
        fields = 'schedule'


class RestaurantWorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantWorker
        fields = ('id', 'name', 'role', 'availability')


class RestaurantMenuEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantMenuEntry
        fields = ('id', 'name', 'price')


class DishRestaurantMenuEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = DishRestaurantMenuEntry
        fields = ('id', 'name', 'price', 'stage', 'weight')


class DrinkRestaurantMenuEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = DrinkRestaurantMenuEntry
        fields = ('id', 'name', 'price', 'contains_alcohol', 'volume')


class RestaurantMenuEntryPolymorphicSerializer(PolymorphicSerializer):
    model_serializer_mapping = {
        RestaurantMenuEntry: RestaurantMenuEntrySerializer,
        DishRestaurantMenuEntry: DishRestaurantMenuEntrySerializer,
        DrinkRestaurantMenuEntry: DrinkRestaurantMenuEntrySerializer
    }


class RestaurantTablePropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantTableProperty
        fields = ('property',)


class RestaurantTableSerializer(serializers.ModelSerializer):
    properties = RestaurantTablePropertySerializer(many=True)

    class Meta:
        model = RestaurantTable
        fields = ('id', 'capacity', 'properties')

    def create(self, validated_data):
        properties_data = validated_data.pop('properties', [])
        restaurant_table = RestaurantTable.objects.create(**validated_data)

        properties = []
        for property_data in properties_data:
            property = RestaurantTableProperty.objects.filter(property=property_data['property']).first()
            if property is not None:
                properties.append(property)

        restaurant_table.properties.set(properties)
        return restaurant_table

