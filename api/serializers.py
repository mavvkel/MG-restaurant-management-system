from rest_framework import serializers
from RMS.models.RestaurantMenuEntry import RestaurantMenuEntry
from RMS.models.DishRestaurantMenuEntry import DishRestaurantMenuEntry
from RMS.models.DrinkRestaurantMenuEntry import DrinkRestaurantMenuEntry
from RMS.models.RestaurantTable import RestaurantTable, RestaurantTableProperty
from RMS.models.RestaurantTableBooking import RestaurantTableBooking
from RMS.models.StartEndHours import StartEndHours
from RMS.models.RestaurantWorker import RestaurantWorker, RestaurantAvailability
from RMS.models.RestaurantWorkerRole import RestaurantWorkerRole
from rest_polymorphic.serializers import PolymorphicSerializer


class RestaurantAvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantAvailability
        fields = 'schedule'


class RestaurantWorkerRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantWorkerRole
        fields = 'role'


class RestaurantWorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantWorker
        fields = ('id', 'roles', 'disabled', 'availability')


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


class StartEndHoursSerializer(serializers.ModelSerializer):
    start_time = serializers.TimeField(format='%H:%M:%S')
    end_time = serializers.TimeField(format='%H:%M:%S')

    class Meta:
        model = StartEndHours
        fields = ('start_time', 'end_time')


class RestaurantTableBookingSerializer(serializers.ModelSerializer):
    startEndHours = StartEndHoursSerializer()
    date = serializers.DateField(format='%Y-%m-%d')

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
