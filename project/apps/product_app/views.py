from rest_framework.viewsets import ModelViewSet

from .models import Product, ImageProduct
from .serializers import ProductSerializer, ImageSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ImageViewSet(ModelViewSet):
    queryset = ImageProduct.objects.all()
    serializer_class = ImageSerializer
