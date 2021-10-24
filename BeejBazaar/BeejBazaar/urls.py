"""BeejBazaar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import views
from rest_framework import routers
from backendAPI.views import SeedList, SeedRetrieveUpdateDestroy, SellerListAPIView, SellerRetrieveUpdateDestroy
from rest_framework.routers import DefaultRouter

from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

router = DefaultRouter()

# router.register('seller', SellerRetrieveAPIView, basename='seller')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', SeedList.as_view()),
    path('api/<int:pk>/', SeedRetrieveUpdateDestroy.as_view()),
    path('api/sellers', SellerListAPIView.as_view()),
    path('api/sellers/<int:pk>/', SellerRetrieveUpdateDestroy.as_view()),
    path('api-token-auth/', obtain_jwt_token),
    path('api-token-refresh/', refresh_jwt_token),
    path('api-token-verify/', verify_jwt_token),
]
