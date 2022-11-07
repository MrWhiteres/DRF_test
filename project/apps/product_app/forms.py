from django.forms import Form, CharField, TextInput, DecimalField, NumberInput, FileField, FileInput
from django.utils.translation import gettext_lazy as _


class ProductAjaxADD(Form):
    uploaded_images = FileField(
        label=_("Upload images"),
        widget=FileInput(
            attrs={
                'class': 'form-control',
                'multiple': "multiple"
            }
        )
    )

    title = CharField(
        label=_("Title"),
        max_length=254,
        widget=TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    price = DecimalField(
        label=_('Price Product'),
        max_digits=9,
        initial=0,
        widget=NumberInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
