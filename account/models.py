from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser

from .manager import UserManager


class User(AbstractUser):
    username = models.CharField(_('username'), max_length=150, unique=False, blank=True, null=True)
    email = models.EmailField(_('email address'), blank=False, unique=True, null=False)

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
