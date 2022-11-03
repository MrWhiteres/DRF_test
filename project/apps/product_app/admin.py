from django.contrib.admin import register, ModelAdmin

from .models import ProductImage, Product


@register(Product)
class ProductAdmin(ModelAdmin):
    list_display = ['owner', 'title', 'price']



@register(ProductImage)
class ImageProductAdmin(ModelAdmin):
    list_display = ['product']