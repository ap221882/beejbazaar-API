from django.db import models
from django.db.models import fields
from .models import SeedItem, Seller
from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework import serializers


class SeedItemSerializer(ModelSerializer):
    category = serializers.StringRelatedField(read_only=True)
    sub_category = serializers.StringRelatedField(read_only=True)
    sellers = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = SeedItem
        fields = [
            'id', 'title', 'info', 'price', 'Rating', 'light', 'watering',
            'time_till_harvest', 'where_to_grow', 'seasonal_information',
            'category', 'sub_category', 'sellers'
        ]
        # fields = '__all__'
        # depth = 2


class SellerSerializer(ModelSerializer):
    seeds = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Seller
        fields = ['id', 'name', 'contactNumber', 'seeds']
        fields = '__all__'
