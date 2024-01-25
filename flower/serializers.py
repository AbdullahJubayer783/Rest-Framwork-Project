from rest_framework import serializers
from . import models

class ColorCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ColorCategoryModel
        fields = '__all__'

class FlowerCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FlowerCategoryModel
        fields = '__all__'

class FlowerSerializer(serializers.ModelSerializer):
    color = serializers.StringRelatedField(many=True)
    flower = serializers.StringRelatedField(many=True)
    class Meta:
        model = models.FlowerModel
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ReviewModel
        fields = '__all__'