from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import serializers
from rest_framework.serializers import Serializer
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser

from .models import SeedItem, Seller

from .serializers import SeedItemSerializer, SellerSerializer
from .models import SeedItem

from rest_framework import generics, mixins

from rest_framework.permissions import IsAuthenticatedOrReadOnly

from rest_framework_jwt.authentication import JSONWebTokenAuthentication


class SeedList(generics.ListAPIView, mixins.CreateModelMixin):
    queryset = SeedItem.objects.all()
    serializer_class = SeedItemSerializer
    authentication_classes = [
        JSONWebTokenAuthentication,
    ]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class SeedRetrieveUpdateDestroy(mixins.DestroyModelMixin,
                                generics.RetrieveAPIView,
                                mixins.UpdateModelMixin):
    queryset = SeedItem.objects.all()
    serializer_class = SeedItemSerializer
    authentication_classes = [
        JSONWebTokenAuthentication,
    ]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class SellerListAPIView(generics.ListAPIView, mixins.CreateModelMixin):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer
    authentication_classes = [
        JSONWebTokenAuthentication,
    ]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class SellerRetrieveUpdateDestroy(mixins.DestroyModelMixin,
                                  generics.RetrieveAPIView,
                                  mixins.UpdateModelMixin):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer
    authentication_classes = [
        JSONWebTokenAuthentication,
    ]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
