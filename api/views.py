from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import status
from rest_framework.permissions import *
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from CMS.models import tempCustomer
from .serializers import *
from RMS.models.DishRestaurantMenuEntry import DishRestaurantMenuEntry
from RMS.models.RestaurantWorker import RestaurantWorker
from RMS.models.Restaurant import Restaurant
from RMS.models.RestaurantTable import RestaurantTable
from RMS.models.DeliveryRestaurantOrder import DeliveryRestaurantOrder
from RMS.models.StationaryRestaurantOrder import StationaryRestaurantOrder
from RMS.models.WeekDay import WeekDay
from RMS.models.StartEndHours import StartEndHours


# @api_view(['GET'])
# def getData(request):
#     items = tempCustomer.objects.all()
#     serializer = tempCustomerSerializer(items, many= True)
#     return Response(serializer.data)
#
# @api_view(['POST'])
# def addItem(request):
#     serializer = tempCustomerSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)

# TODO: TokenAuthentication should have the keyword set to 'bearer'

class RestaurantMenuEntryListView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = DishRestaurantMenuEntrySerializer
    queryset = DishRestaurantMenuEntry.objects.all()


# TODO: status 409
class RestaurantMenuEntryDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
    serializer_class = DishRestaurantMenuEntrySerializer
    queryset = DishRestaurantMenuEntry.objects.all()


class RestaurantWorkerListView(generics.ListCreateAPIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = RestaurantWorkerSerializer
    queryset = RestaurantWorker.objects.all()


class RestaurantWorkerDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = RestaurantWorkerSerializer
    queryset = RestaurantWorker.objects.all()


class RestaurantView(generics.RetrieveUpdateAPIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = RestaurantSerializer
    queryset = Restaurant.objects.all()


class RestaurantTableListView(generics.ListCreateAPIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = RestaurantTableSerializer
    queryset = RestaurantTable.objects.all()


class RestaurantTableDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = RestaurantTableSerializer
    queryset = RestaurantTable.objects.all()


class RestaurantDeliveryRestaurantOrderView(generics.ListCreateAPIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = DeliveryRestaurantOrderSerializer
    queryset = DeliveryRestaurantOrder.objects.all()


class RestaurantDeliveryRestaurantOrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = DeliveryRestaurantOrderSerializer
    queryset = DeliveryRestaurantOrder.objects.all()


class StationaryRestaurantOrderView(generics.ListCreateAPIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = StationaryRestaurantOrderSerializer
    queryset = StationaryRestaurantOrder.objects.all()


class StationaryRestaurantDetailOrderView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = StationaryRestaurantOrderSerializer
    queryset = StationaryRestaurantOrder.objects.all()


class RestaurantAvailabilityView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = RestaurantAvailabilitySerializer
    queryset = RestaurantAvailability.objects.all()


class StartEndHoursView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = StartEndHoursSerializer
    queryset = StartEndHours.objects.all()


class WeekDayView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = WeekDaySerializer
    queryset = WeekDay
