from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers
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


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = models.ReviewModel.objects.all()
    serializer_class = serializers.ReviewSerializer

