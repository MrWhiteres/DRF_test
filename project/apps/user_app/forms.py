from django import forms
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.forms import (
    UserCreationForm as DjangoUserCreationForm,
    AuthenticationForm as DjangoAuthenticationForm,
)
from django.forms import EmailField, CharField, TextInput, PasswordInput
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class UserCreationForm(DjangoUserCreationForm):
    """
    New user registration form.
    """
    email = EmailField(
        label=_("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={"autocomplete": "email", 'class': 'form-control'}),
        help_text='Enter a valid email address'
    )
    username = CharField(
        label=_("Username"),
        max_length=20,
        widget=TextInput(attrs={'class': 'form-control'})
    )

    first_name = CharField(
        label=_("First name"),
        max_length=20,
        widget=TextInput(attrs={'class': 'form-control'})
    )

    last_name = CharField(
        label=_("Last name"),
        max_length=20,
        widget=TextInput(attrs={'class': 'form-control'})
    )

    password1 = CharField(
        widget=PasswordInput(attrs={'class': 'form-control'})
    )

    password2 = forms.CharField(
        widget=PasswordInput(attrs={'class': 'form-control'})
    )

    class Meta(DjangoUserCreationForm.Meta):
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        ]


class AuthenticationForm(DjangoAuthenticationForm):
    """
    Base user form for authentication.
    """

    def clean(self):
        """
        The function takes values from the form and checks
         its validity and the existence of a user with such data.
        """
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username is not None and password:
            self.user_cache = authenticate(
                self.request,
                username=username,
                password=password,
            )
            if self.user_cache is None:
                raise self.get_invalid_login_error()
            else:
                self.confirm_login_allowed(self.user_cache)
        return self.cleaned_data
