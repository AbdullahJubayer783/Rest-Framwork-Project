from rest_framework import serializers
from . import models

class OrderDetailsSerializer(serializers.ModelSerializer):
    # flower = serializers.StringRelatedField(many=False)
    # user = serializers.StringRelatedField(many=False)
    class Meta:
        model = models.OrderDetails
        fields = '__all__'