from django.contrib.admin import register, ModelAdmin

from .models import ImageProduct, Product


@register(Product)
class ProductAdmin(ModelAdmin):
    list_display = ['owner', 'title', 'price']



@register(ImageProduct)
class ImageProductAdmin(ModelAdmin):
    list_display = ['product']