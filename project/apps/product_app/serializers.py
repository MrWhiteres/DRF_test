from rest_framework.serializers import ModelSerializer, ListField, FileField, ImageField
from rest_framework.utils import model_meta

from .models import Product, ProductImage
from ..user_app.models import User


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
        if type(validated_data['owner']) in (str, int):
            validated_data['owner'] = User.objects.get(pk=validated_data['owner'])
        uploaded_data = validated_data.pop('uploaded_images', None)
        if not uploaded_data:
            uploaded_data = self.context.get('request').FILES.getlist('uploaded_images')
        new_product = Product.objects.create(**validated_data)
        if uploaded_data:
            for uploaded_item in uploaded_data:
                modified_data = modify_input_for_multiple_files(new_product.id, uploaded_item)
                file_serializer = ImageSerializer(data=modified_data)
                file_serializer.is_valid()
                if file_serializer.is_valid():
                    file_serializer.save()
            return new_product
        return new_product.delete()

    def update(self, instance, validated_data):
        info = model_meta.get_field_info(instance)
        uploaded_data = validated_data.pop('uploaded_images', None)
        m2m_fields = []
        for attr, value in validated_data.items():
            if attr in info.relations and info.relations[attr].to_many:
                m2m_fields.append((attr, value))
            else:
                setattr(instance, attr, value)

        instance.save()

        if uploaded_data:
            for uploaded_item in uploaded_data:
                modified_data = modify_input_for_multiple_files(instance.id, uploaded_item)
                file_serializer = ImageSerializer(data=modified_data)
                if file_serializer.is_valid():
                    file_serializer.save()

        for attr, value in m2m_fields:
            field = getattr(instance, attr)
            field.set(value)

        return instance


def modify_input_for_multiple_files(product, images):
    dict = {}
    dict['product'] = product
    dict['images'] = images
    return dict
