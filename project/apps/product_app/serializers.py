from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Product, ImageProduct


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class ImageSerializer(ModelSerializer):
    class Meta:
        model = ImageProduct
        fields = "__all__"
