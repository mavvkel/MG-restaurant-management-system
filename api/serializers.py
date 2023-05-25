from abc import ABC

from rest_framework import serializers
from django.utils import timezone

from RMS.models.StartEndHours import StartEndHours
from RMS.models.DishRestaurantMenuEntry import DishRestaurantMenuEntry
from CMS.models import tempCustomer
from RMS.models.RestaurantWorker import RestaurantWorker
from RMS.models.Restaurant import Restaurant
from RMS.models.DeliveryRestaurantOrder import DeliveryRestaurantOrder
from RMS.models.StationaryRestaurantOrder import StationaryRestaurantOrder
from RMS.models.RestaurantAvailability import RestaurantAvailability
from RMS.models.WeekDay import WeekDay


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


class RestaurantAvailabilityListSerializer(serializers.ListSerializer):
    def update(self, instance, validated_data):
        weekday_mapping = {element.id: element for element in instance}
        startend_hours_mapping = {item['id']: item for item in validated_data}

        ret = []
        for weekday_id, data in startend_hours_mapping.items():
            weekday = weekday_mapping.get(weekday_id, None)
            if weekday is None:
                ret.append(self.child.create(data))
            else:
                ret.append(self.child.update(weekday, data))

        # Perform deletions.
        for weekday_id, weekday in weekday_mapping.items():
            if weekday_id not in startend_hours_mapping:
                weekday.delete()

        return ret


class StartEndHoursSerializer(serializers.ModelSerializer):
    start_time = serializers.DateTimeField(format="%H:%M:%S")
    end_time = serializers.DateTimeField(format="%H:%M:%S")

    class Meta:
        model = StartEndHours
        fields = ['start_time', 'end_time']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['start_time'] = instance.start_time.strftime("%H:%M:%S")
        representation['end_time'] = instance.end_time.strftime("%H:%M:%S")
        return representation


class WeekDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = WeekDay
        fields = '__all__'


class RestaurantAvailabilitySerializer(serializers.ModelSerializer):
    schedule = serializers.DictField()

    class Meta:
        # list_serializer_class = RestaurantAvailabilityListSerializer
        model = RestaurantAvailability
        fields = '__all__'
