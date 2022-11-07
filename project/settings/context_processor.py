from project.apps.product_app.forms import ProductAjaxADD
from project.apps.product_app.serializers import ProductSerializer


def get_context_data(request):
    context = {
        'product_ajax': ProductAjaxADD(),
    }
    return context
