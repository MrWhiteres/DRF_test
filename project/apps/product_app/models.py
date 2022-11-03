from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Model, CharField, DecimalField, ImageField, ForeignKey, CASCADE, DateTimeField

from project.apps.user_app.models import User


def path_to_img(instance, filename):
    try:
        return f"product_img/{instance.product.title}-{ImageProduct.objects.latest('id').id + 1}-{filename[-4:]}"
    except ObjectDoesNotExist:
        return f"product_img/{instance.product.title}-1-{filename[-4:]}"


class Product(Model):
    title = CharField(max_length=255, verbose_name="Product Title")
    price = DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='Product Price')
    owner = ForeignKey(User, on_delete=CASCADE)
    created_date = DateTimeField(auto_now_add=True)
    update_date = DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title)


class ImageProduct(Model):
    product = ForeignKey(Product, on_delete=CASCADE)
    image = ImageField(upload_to=path_to_img)

    def __str__(self):
        try:
            return f'{str(self.product)}-{str({ImageProduct.objects.latest("id").id + 1})}'
        except ObjectDoesNotExist:
            return f'{str(self.product)}-1'