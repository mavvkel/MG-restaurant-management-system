from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import status
from rest_framework.permissions import *
from rest_framework.authentication import BasicAuthentication
from CMS.models import tempCustomer
from RMS.models import RestaurantMenuEntry
from .serializers import *
from RMS.models.DishRestaurantMenuEntry import DishRestaurantMenuEntry
from RMS.models.DrinkRestaurantMenuEntry import DrinkRestaurantMenuEntry
from rest_framework.authentication import TokenAuthentication
from itertools import chain


class BearerAuthentication(TokenAuthentication):
    keyword = 'Bearer'


@api_view(['GET'])
def getData(request):
    items = tempCustomer.objects.all()
    serializer = tempCustomerSerializer(items, many= True)
    return Response(serializer.data)

@api_view(['POST'])
def addItem(request):
    serializer = tempCustomerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


class RestaurantMenuEntryListView(generics.ListCreateAPIView):
    authentication_classes = [BearerAuthentication, BasicAuthentication]
    permission_classes = []
    serializer_class = DishRestaurantMenuEntrySerializer
    queryset = DishRestaurantMenuEntry.objects.all()
    # queryset = RestaurantMenuEntry.objects.instance_of(DrinkRestaurantMenuEntry) \
    #     | RestaurantMenuEntry.objects.instance_of(DishRestaurantMenuEntry.objects)


# TODO: status 409
class RestaurantMenuEntryDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [BearerAuthentication]
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
    serializer_class = DishRestaurantMenuEntrySerializer
    queryset = DishRestaurantMenuEntry.objects.all()
