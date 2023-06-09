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
    authentication_classes = []
    permission_classes = []
    serializer_class = RestaurantMenuEntryPolymorphicSerializer
    queryset = RestaurantMenuEntry.objects.all()


# TODO: status 409
class RestaurantMenuEntryDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [BearerAuthentication]
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
    serializer_class = DishRestaurantMenuEntrySerializer
    queryset = DishRestaurantMenuEntry.objects.all()


class RestaurantTableListView(generics.ListCreateAPIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = RestaurantTableSerializer
<<<<<<< Updated upstream
    queryset = RestaurantTable.objects.all()
=======
    queryset = RestaurantTable.objects.all()


class RestaurantTablePropertyView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = RestaurantTablePropertySerializer
    queryset = RestaurantTableProperty.objects.all()

class RestaurantOrderView(generics.ListCreateAPIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = RestaurantOrderSerializer
    queryset = RestaurantOrder.objects.all()


class RestaurantOrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = RestaurantOrderSerializer
    queryset = RestaurantOrder.objects.all()

>>>>>>> Stashed changes
