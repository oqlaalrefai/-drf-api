from django.shortcuts import render
from rest_framework import generics
from .searilizers import OrderSerialzer
from .models import order


class orderList(generics.ListCreateAPIView):
    # queryset = Country.objects.filter(published = True)
    queryset = order.objects.all()
    serializer_class = OrderSerialzer


class orderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = order.objects.all()
    serializer_class = OrderSerialzer