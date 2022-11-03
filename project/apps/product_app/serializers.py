from rest_framework.serializers import ModelSerializer, ListField, FileField, ImageField

from .models import Product, ProductImage


class ImageSerializer(ModelSerializer):
    images = ImageField()

    class Meta:
        model = ProductImage
        fields = ['product', 'images']


class ProductSerializer(ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)
    uploaded_images = ListField(
        child=FileField(max_length=1000000, allow_empty_file=False, use_url=False), write_only=True
    )

    class Meta:
        model = Product
        fields = ["title", 'price', 'created_date', 'update_date', 'owner', 'images', 'uploaded_images']

    def create(self, validated_data):
        uploaded_data = validated_data.pop('uploaded_images')
        new_product = Product.objects.create(**validated_data)
        for uploaded_item in uploaded_data:
            modified_data = modify_input_for_multiple_files(new_product.id, uploaded_item)
            file_serializer = ImageSerializer(data=modified_data)
            if file_serializer.is_valid():
                file_serializer.save()
        return new_product


def modify_input_for_multiple_files(product, images):
    dict = {}
    dict['product'] = product
    dict['images'] = images
    return dict
