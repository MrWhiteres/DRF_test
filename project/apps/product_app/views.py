from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect
from rest_framework.generics import ListAPIView, DestroyAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Product, ImageProduct
from .serializers import ProductSerializer, FullSerializer


class Base(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ListProductPageView(ListAPIView):
    renderer_classes = (TemplateHTMLRenderer,)
    template_name = 'base.html'
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        product = Product.objects.all()
        serializer = self.get_serializer(product)
        return Response({'serializer': serializer, 'products': product})


class ProductDetail(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'product_detail.html'

    def get_object(self, pk):
        try:
            return Product.objects.get(id=pk)
        except ObjectDoesNotExist:
            return None

    def get(self, request, pk, *args, **kwargs):
        product = self.get_object(pk)
        image = ImageProduct.objects.filter(product=product.id) if product else None
        serializer = FullSerializer(data=request.data)
        serializer.is_valid()
        return Response({'serializer': serializer, 'product': product,
                         'image': image})


class ProductDelete(DestroyAPIView):
    def get_object(self, pk):
        return Product.objects.get(id=pk) if Product.objects.get(id=pk) else None

    def post(self, request, pk, *args, **kwargs):
        product = self.get_object(pk)
        product.delete()
        return redirect('product_detail', pk=pk)


class ProductCreate(CreateAPIView):
    parser_classes = [MultiPartParser, FormParser, FileUploadParser]
    serializer_class = FullSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'create.html'

    def get(self, request, *args, **kwargs):
        serializer = FullSerializer(data=request.data)
        serializer.is_valid()
        return Response({'serializer': serializer})

    def post(self, request, *args, **kwargs):
        serializer = FullSerializer(data=request.data)
        serializer.is_valid()
        serializer.create(validated_data=serializer.data)
        return Response({'serializer': serializer})
