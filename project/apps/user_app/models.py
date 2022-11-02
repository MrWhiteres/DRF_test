from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, EmailField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """
    New user model.
    """

    username = CharField(_("username"), max_length=20, unique=True)
    email = EmailField(_('email address'), unique=True)
    first_name = CharField(_("first_name"), max_length=20)
    last_name = CharField(_("last_name"), max_length=20)

    @property
    def get_absolute_url(self):
        return reverse('profile', kwargs={'pk': self.id})

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = 'Профиль'
