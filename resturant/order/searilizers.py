from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers
from .models import order


class OrderSerialzer(serializers.ModelSerializer):
    class Meta:
        fields = ['foodName', 'content', 'times']
        model = order