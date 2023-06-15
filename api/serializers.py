from rest_framework import serializers
from RMS.models.RestaurantMenuEntry import RestaurantMenuEntry
from RMS.models.DishRestaurantMenuEntry import DishRestaurantMenuEntry
from RMS.models.DrinkRestaurantMenuEntry import DrinkRestaurantMenuEntry
from RMS.models.RestaurantOrder import RestaurantOrder, MenuSelection
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
            property = RestaurantTableProperty.objects.create(property=property_data['property'])
            if property is not None:
                properties.append(property)

        restaurant_table.properties.set(properties)
        return restaurant_table


class ContactDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactData
        fields = ('name', 'phone', 'email', 'chatId')


class MenuSelectionSerializer(serializers.ModelSerializer):
    menu_entry_id = serializers.PrimaryKeyRelatedField(queryset=RestaurantMenuEntry.objects.all())

    class Meta:
        model = MenuSelection
        fields = ['id', 'menu_entry_id', 'count']


class RestaurantOrderSerializer(serializers.ModelSerializer):
    menu_selection = MenuSelectionSerializer(many=True)
    customer_contact_data = ContactDataSerializer()

    class Meta:
        model = RestaurantOrder
        fields = ('id', 'customer_contact_data', 'menu_selection', 'date')

    def create(self, validated_data):
        menu_selection_data = validated_data.pop('menu_selection', [])
        contact_data = validated_data.pop('customer_contact_data', {})
        menu_selections = []

        for selection_data in menu_selection_data:
            menu_entry_id = selection_data.get('menu_entry_id')
            count = selection_data.get('count')
            menu_selection, _ = MenuSelection.objects.get_or_create(menu_entry_id=menu_entry_id, count=count)
            menu_selections.append(menu_selection)

        contact_data_instance = ContactData.objects.create(**contact_data)

        restaurant_order = RestaurantOrder.objects.create(
            customer_contact_data=contact_data_instance,
            **validated_data
        )
        restaurant_order.menu_selection.set(menu_selections)

        return restaurant_order

class StartEndHoursSerializer(serializers.ModelSerializer):
    start_time = serializers.TimeField(format='%H:%M:%S')
    end_time = serializers.TimeField(format='%H:%M:%S')

    class Meta:
        model = StartEndHours
        fields = ('start_time', 'end_time')


class RestaurantTableBookingSerializer(serializers.ModelSerializer):
    startEndHours = StartEndHoursSerializer()
    date = serializers.DateTimeField(format='%Y-%m-%d')

    class Meta:
        model = RestaurantTableBooking
        fields = ('id', 'table', 'startEndHours', 'date')

    def create(self, validated_data):
        start_end_hours_data = validated_data.pop('startEndHours')
        table_data = validated_data.pop('table')
        if table_data is None:
            print("ERROR: COULDN'T FIND THE TABLE")
            quit()
        # Create or retrieve the related objects
        start_end_hours = StartEndHours.objects.create(**start_end_hours_data)

        # Create the RestaurantTableBooking object
        booking = RestaurantTableBooking.objects.create(
            startEndHours=start_end_hours,
            table=table_data,
            **validated_data
        )

        return booking
