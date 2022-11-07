from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.shortcuts import redirect
from rest_framework.decorators import action
from rest_framework.generics import ListAPIView, DestroyAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Product, ProductImage
from .serializers import ProductSerializer


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
        product = self.get_object(pk=pk)
        image = ProductImage.objects.filter(product=product.id) if product else None
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid()
        return Response({'serializer': serializer, 'product': product,
                         'image': image})


class ProductDelete(DestroyAPIView):
    serializer_class = ProductSerializer
    def get_object(self, pk):
        return Product.objects.get(id=pk) if Product.objects.get(id=pk) else None

    @action(methods=['DELETE'], detail=True)
    def post(self, request, pk, *args, **kwargs):
        product = self.get_object(pk)
        product.delete()
        return redirect('list_page')


class ProductCreate(CreateAPIView):
    parser_classes = [MultiPartParser, FormParser, FileUploadParser]
    serializer_class = ProductSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'create.html'

    def get(self, request, *args, **kwargs):
        count_product = len(Product.objects.all()) if Product.objects.all() else 0
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid()
        return Response({'serializer': serializer, 'count_product': count_product})

    @action(methods=["POST"], detail=True)
    def create_object(self, request, *args, **kwargs):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid()
        serializer.create(validated_data=serializer.data)
        return Response(status=201)


class ProductUpdate(UpdateAPIView):
    parser_classes = [MultiPartParser, FormParser, FileUploadParser]
    serializer_class = ProductSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'product_update.html'

    def get_object(self, pk):
        return Product.objects.get(id=pk) if Product.objects.get(id=pk) else None

    def get(self, request, pk, *args, **kwargs):
        product = self.get_object(pk=pk)
        image = ProductImage.objects.filter(product=product.id) if product else None
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid()
        return Response({'serializer': serializer, 'product': product,
                         'image': image})

    @action(methods=["PUT"], detail=True)
    def post(self, request, pk, *args, **kwargs):
        product = self.get_object(pk=pk)
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid()
        serializer.update(instance=product, validated_data=serializer.data)
        return redirect('product_detail', pk=pk)


class CreateProductAjaxView(CreateAPIView):
    parser_classes = [MultiPartParser, FormParser, FileUploadParser]
    serializer_class = ProductSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'create.html'

    def get(self, request, *args, **kwargs):
        count_product = len(Product.objects.all()) if Product.objects.all() else 0
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid()
        return Response({'serializer': serializer, 'count_product': count_product})

    def post(self, request, *args, **kwargs):
        serializer = ProductSerializer(data=request.data, context={'request': request})
        serializer.is_valid()
        if serializer.is_valid():
            result = serializer.create(validated_data=serializer.data)
            if result:
                return JsonResponse(
                    data={
                        'status': 201,
                    },
                    status=200
                )
            return JsonResponse(
                data={
                    'status': 400,
                },
                status=400
            )
        else:
            return JsonResponse(
                data={
                    'status': 400
                },
                status=200
            )
