from rest_framework import serializers
from RMS.models.RestaurantMenuEntry import RestaurantMenuEntry
from RMS.models.DishRestaurantMenuEntry import DishRestaurantMenuEntry
from RMS.models.DrinkRestaurantMenuEntry import DrinkRestaurantMenuEntry
from RMS.models.RestaurantOrder import RestaurantOrder
from RMS.models.RestaurantTable import RestaurantTable, RestaurantTableProperty
from RMS.models.RestaurantTableBooking import RestaurantTableBooking
from RMS.models.StartEndHours import StartEndHours
from RMS.models.RestaurantWorker import RestaurantWorker, RestaurantAvailability
from CMS.models import tempCustomer
from RMS.models.ContactData import ContactData

from rest_polymorphic.serializers import PolymorphicSerializer
from datetime import datetime


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


class ContactDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactData
        fields = ('name', 'phone', 'email', 'chatId')


class RestaurantOrderSerializer(serializers.ModelSerializer):
    customerContactData = ContactDataSerializer()
    menuSelection = serializers.DictField(child=serializers.IntegerField())

    def create(self, validated_data):
        contact_data_data = validated_data.pop('customerContactData')
        menu_selection_data = validated_data.pop('menuSelection')

        order = RestaurantOrder.objects.create(**validated_data)

        contact_data = ContactData.objects.create(order=order, **contact_data_data)

        for menu_entry, count in menu_selection_data.items():
            order.addOrUpdateMenuEntry(menu_entry, count)

        return order

    def update(self, instance, validated_data):
        contact_data_data = validated_data.pop('customerContactData')
        menu_selection_data = validated_data.pop('menuSelection')

        instance = super().update(instance, validated_data)

        contact_data = instance.getCustomerContactData()
        if contact_data:
            contact_data.setName(contact_data_data.get('name', contact_data.getName()))
            contact_data.setPhone(contact_data_data.get('phone', contact_data.getPhone()))
            contact_data.setEmail(contact_data_data.get('email', contact_data.getEmail()))
            contact_data.setChatId(contact_data_data.get('chatId', contact_data.getChatId()))
            contact_data.save()

        for menu_entry, count in menu_selection_data.items():
            instance.addOrUpdateMenuEntry(menu_entry, count)

        return instance

class StartEndHoursSerializer(serializers.ModelSerializer):
    start_time = serializers.TimeField(format='%H:%M:%S')
    end_time = serializers.TimeField(format='%H:%M:%S')

    class Meta:
        model = StartEndHours
        fields = ('start_time', 'end_time')


class RestaurantTableBookingSerializer(serializers.ModelSerializer):
    startEndHours = StartEndHoursSerializer()
    table = RestaurantTableSerializer()
    date = serializers.DateTimeField(format='%Y-%m-%d')

    class Meta:
        model = RestaurantTableBooking
        fields = ('id', 'table', 'startEndHours', 'date')

    def create(self, validated_data):
        start_end_hours_data = validated_data.pop('startEndHours')
        table_data = validated_data.pop('table')
        table_properties = table_data['properties']

        # Create or retrieve the related objects
        start_end_hours = StartEndHours.objects.create(**start_end_hours_data)
        table = RestaurantTable.objects.create(capacity=table_data['capacity'])
        for property_data in table_properties:
            table.properties.add(RestaurantTableProperty.objects.create(property=property_data['property']))

        # Create the RestaurantTableBooking object
        booking = RestaurantTableBooking.objects.create(
            startEndHours=start_end_hours,
            table=table,
            **validated_data
        )

        return booking
