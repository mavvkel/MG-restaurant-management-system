from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, APIView
from CMS.models import tempCustomer
from RMS.models import RestaurantTable, Restaurant
from .serializers import RestaurantTableSerializer, RestaurantSerializer
from rest_framework import status


# RMS API commands

class RestaurantTableAPI(APIView):
    def get(self, request, format=None):
        items = RestaurantTable.objects.all()
        serializer = RestaurantTableSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def get(self, request, _id, format=None):
        items = RestaurantTable.objects.all().filter(__id__=_id)
        serializer = RestaurantTableSerializer(items, many=False)
        if items is None:
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request, format=None):
        serializer = RestaurantTableSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # how to check if a serializer saved a value
            # We don't need to check if it didn't create a new instance since save already
            # updates the content if it does exist
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, _id, format=None):
        items = RestaurantTable.objects.all().filter(__id__=_id)
        serializer = RestaurantTableSerializer(items, data=request.data)
        if items is None:
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        snippet = RestaurantTable.objects.all().filter(__id__=id)
        if snippet is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        snippet.delete()
        return Response(status=status.HTTP_200_OK)


class RestaurantAPI(APIView):
    def get(self, request, format=None):
        items = Restaurant.objects.all()
        serializer = RestaurantSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def get(self, request, id, format=None):
        items = Restaurant.objects.all().filter(__id__=id)
        serializer = RestaurantSerializer(items, many=False)
        if items is None:
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id, format=None):
        items = Restaurant.objects.all().filter(__id__=id)
        serializer = RestaurantSerializer(items, data=request.data)
        if items is None:
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

# Create your views here.
