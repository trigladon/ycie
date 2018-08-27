from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from ..managers import UserManager


__all__ = (
    'User',
)


class User(AbstractUser):
    """
    User model
    """
    username = models.CharField(_('Username'), max_length=150, unique=False, blank=True, null=True)
    email = models.EmailField(_('Email address'), blank=False, unique=True, null=False)
    phone_number = models.CharField(_('Phone number'), blank=False, null=False, max_length=12)
    address = models.CharField(_('Address'), null=True, blank=True, max_length=1023)
    zip = models.IntegerField(_('Zip code'), null=True, blank=True)
    city_id = models.ForeignKey('City', null=True, blank=True, on_delete=models.SET_NULL)

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'

    def to_dict(self):
        return {
            'id': self.pk,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'is_active': self.is_active,
            'is_staff': self.is_staff,
            'date_joined': self.date_joined
        }


