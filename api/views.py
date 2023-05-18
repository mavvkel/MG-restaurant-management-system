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


# TODO: TokenAuthentication should have the keyword set to 'bearer'
class RestaurantMenuEntryListView(generics.ListCreateAPIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = DishRestaurantMenuEntrySerializer
    queryset = DishRestaurantMenuEntry.objects.all()


# TODO: status 409
class RestaurantMenuEntryDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
    serializer_class = DishRestaurantMenuEntrySerializer
    queryset = DishRestaurantMenuEntry.objects.all()
