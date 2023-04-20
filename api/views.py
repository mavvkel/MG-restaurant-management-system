from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, APIView
from CMS.models import tempCustomer
from RMS.models import RestaurantTable, Restaurant
from .serializers import tempCustomerSerializer
from rest_framework import status

# RMS API commands

class RestaurantTableAPI(APIView):
    def get(self, request, format=None):
        items = RestaurantTable.objects.all()
        serializer = tempCustomerSerializer(items, many=True)
        return Response(serializer.data)

    def get(self, request, id, format=None):
        items = RestaurantTable.objects.all().filter(__id__=id)
        serializer = tempCustomerSerializer(items, many=False)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = tempCustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    def put(self, request, id, format=None):
        items = RestaurantTable.objects.all().filter(__id__=id)
        serializer = tempCustomerSerializer(items, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    def delete(self, request, id, format=None):
        snippet = RestaurantTable.objects.all().filter(__id__=id)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class RestaurantAPI(APIView):
    def get(self, request, format=None):
        items = Restaurant.objects.all()
        serializer = tempCustomerSerializer(items, many=True)
        return Response(serializer.data)

    def get(self, request, id, format=None):
        items = Restaurant.objects.all().filter(__id__=id)
        serializer = tempCustomerSerializer(items, many=False)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = tempCustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    def put(self, request, id, format=None):
        items = Restaurant.objects.all().filter(__id__=id)
        serializer = tempCustomerSerializer(items, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    def delete(self, request, id, format=None):
        snippet = Restaurant.objects.all().filter(__id__=id)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Create your views here.
