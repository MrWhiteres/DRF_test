from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import DetailView

from .forms import UserCreationForm, AuthenticationForm
from .models import User


class Register(View):
    """
    Views for new user registration.
    """
    template_name = 'registration/register.html'

    def get(self, request):
        """
        Base method for views registration.
        """
        context = {
            'form': UserCreationForm(),
        }
        return render(request, self.template_name, context)

    def post(self, request):
        """
        Registration method with data validation and subsequent sending of a message to the mail.
        """
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            login_user = authenticate(username=username, password=password)
            login(request, login_user)
            return redirect('base_page')
        context = {
            'form': form,
        }
        return render(request, self.template_name, context)


class ProfileView(DetailView):
    """
    User profile views.
    """
    model = User
    context_object_name = 'profile'
    template_name = 'profile.html'


class MyLoginView(LoginView):  # pylint: disable=too-many-ancestors
    """
    Login views.
    """
    form_class = AuthenticationForm
