from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.
class ColorCategoryViewSet(viewsets.ModelViewSet):
    queryset = models.ColorCategoryModel.objects.all()
    serializer_class = serializers.ColorCategorySerializer


class FlowerCategoryViewSet(viewsets.ModelViewSet):
    queryset = models.FlowerCategoryModel.objects.all()
    serializer_class = serializers.FlowerCategorySerializer


class FlowerViewSet(viewsets.ModelViewSet):
    queryset = models.FlowerModel.objects.all()
    serializer_class = serializers.FlowerSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title','color__name','flower__name',]
   
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = models.ReviewModel.objects.all()
    serializer_class = serializers.ReviewSerializer

