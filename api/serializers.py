from rest_framework import serializers
from CMS.models import tempCustomer

class tempCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = tempCustomer
        fields = '__all__'
