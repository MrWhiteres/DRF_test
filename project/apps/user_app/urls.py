from django.urls import path, include

from project.apps.user_app.views import ProfileView, Register

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('profile/<int:pk>', ProfileView.as_view(), name='profile'),
    path('register/', Register.as_view(), name='register'),
]
