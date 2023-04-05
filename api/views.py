from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from CMS.models import tempCustomer
from .serializers import tempCustomerSerializer

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

# Create your views here.
