"""settings URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from .apps.product_app.views import ListProductPageView, ProductDetail, ProductDelete, ProductCreate, ProductUpdate, \
    CreateProductAjaxView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('jet/', include('jet.urls', 'jet')),
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('auth/', include('project.apps.user_app.urls')),
    path('product/', ListProductPageView.as_view(), name='list_page'),
    path('product/<pk>/', ProductDetail.as_view(), name='product_detail'),
    path('', ProductCreate.as_view(), name='create_page'),
    path('product_update/<pk>/', ProductUpdate.as_view(), name='update_page'),
    path('product_delete/<pk>/', ProductDelete.as_view(), name='delete_page'),
    path('product_create/', CreateProductAjaxView.as_view(), name='product_ajax'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
