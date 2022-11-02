from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter

from .views import ProductViewSet, ImageViewSet

router = DefaultRouter()
router.register("product", ProductViewSet)
router.register("image", ImageViewSet)

urlpatterns = [
    path('', TemplateView.as_view(template_name='base.html'), name='base_page'),
    path("product/", include(router.urls)),
    path("api/", include("rest_framework.urls", namespace="rest_framework")),
]

