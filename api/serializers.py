from rest_framework import serializers
from RMS.models.RestaurantMenuEntry import RestaurantMenuEntry
from RMS.models.DishRestaurantMenuEntry import DishRestaurantMenuEntry
from RMS.models.DrinkRestaurantMenuEntry import DrinkRestaurantMenuEntry
<<<<<<< Updated upstream
from RMS.models.RestaurantTable import RestaurantTable
=======
from RMS.models.RestaurantTable import RestaurantTable, RestaurantTableProperty
from RMS.models.RestaurantOrder import RestaurantOrder
>>>>>>> Stashed changes
from CMS.models import tempCustomer
from rest_polymorphic.serializers import PolymorphicSerializer



class tempCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = tempCustomer
        fields = '__all__'


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


class RestaurantTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantTable
        fields = ('id', 'capacity', 'properties')
<<<<<<< Updated upstream
=======

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
>>>>>>> Stashed changes
