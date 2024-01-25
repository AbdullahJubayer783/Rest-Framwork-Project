from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers
# Create your views here.
class OrderDetailsViewSet(viewsets.ModelViewSet):
    queryset = models.OrderDetails.objects.all()
    serializer_class = serializers.OrderDetailsSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        user_id = self.request.query_params.get("user_id")
        if user_id:
            queryset = queryset.filter(user_id=user_id)
        return queryset