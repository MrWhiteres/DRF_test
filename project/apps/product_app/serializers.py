from rest_framework.fields import ImageField, ListField
from rest_framework.serializers import ModelSerializer, Serializer

from .models import Product, ImageProduct


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ["title", 'price', 'created_date', 'update_date', 'owner']


class ImageSerializer(ModelSerializer):
    class Meta:
        model = ImageProduct
        fields = ["image", 'product']


class MultipleImageSerializer(Serializer):
    images = ListField(
        child=ImageField()
    )


class FullSerializer(ModelSerializer):
    image = ImageSerializer()

    class Meta:
        model = Product
        fields = '__all__'

    def create(self, validated_data):
        pass
