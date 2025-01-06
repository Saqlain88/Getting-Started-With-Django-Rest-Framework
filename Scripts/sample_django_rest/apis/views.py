from django.shortcuts import render

from rest_framework import viewsets

from .serializers import CustomerSerializer
from .models import CustomerModel

class CustomerViewSet(viewsets.ModelViewSet):

    queryset = CustomerModel.objects.all()

    serializer_class = CustomerSerializer