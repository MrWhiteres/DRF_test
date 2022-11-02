from django.contrib.admin import register, ModelAdmin

from .models import ImageProduct, Product


@register(Product)
class ProductAdmin(ModelAdmin):
    list_display = ['owner', 'title', 'price']

    def save_model(self, request, obj, form, change):
        if not obj.owner:
            obj.owner = request.user
        obj.save()


@register(ImageProduct)
class ImageProductAdmin(ModelAdmin):
    list_display = ['product']