from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

from memoized_property import memoized_property

from .manager import UserManager
from .constants import *


class User(AbstractUser):
    username = models.CharField(_('username'), max_length=150, unique=False, blank=True, null=True)
    email = models.EmailField(_('email address'), blank=False, unique=True, null=False)

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'

    @memoized_property
    def contacts(self):
        return Contact.objects. \
            filter(id_object=self.pk). \
            filter(model_type=CONTACT_MODEL_USER). \
            all()

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


class Role(models.Model):
    name = models.CharField(_('Name'), max_length=15, null=False)
    title = models.CharField(_('Title'), max_length=15, unique=True, null=False)

    class Meta:
        verbose_name = _("Role")
        verbose_name_plural = _("Roles")

    def to_dict(self):
        return {
            'id': self.pk,
            'name': self.name,
            'title': self.title,
        }


class Contact(models.Model):
    TYPES = (
        (CONTACT_TYPE_EMAIL, _('Email')),
        (CONTACT_TYPE_FAX, _('FAX')),
        (CONTACT_TYPE_LEGAL_ADDRESS, _('Legal address')),
        (CONTACT_TYPE_PHYSICAL_ADDRESS, _('Physical address')),
    )

    MODEL_TYPES = (
        (CONTACT_MODEL_COMPANY, _('Company')),
        (CONTACT_MODEL_USER, _('User'))
    )

    id_object = models.IntegerField(_('Id object'), blank=False, null=False)
    type = models.CharField(_('Type'), choices=TYPES, null=False, max_length=20)
    model = models.CharField(_('Model'), choices=MODEL_TYPES, null=False, max_length=20)
    data = models.CharField(_('Data'), null=False, max_length=1023)
    create_date = models.DateTimeField(_('Create date'), default=timezone.now)

    class Meta:
        verbose_name = _("Contact")
        verbose_name_plural = _("Contacts")

    def to_dict(self):
        return {
            'id': self.pk,
            'id_object': self.id_object,
            'type': self.type,
            'model': self.model,
            'data': self.data,
            'create_date': self.create_date
        }


class Company(models.Model):
    name = models.CharField(_('Organization name'), max_length=511, null=False)
    unp = models.CharField(_('UNP'), max_length=15, null=False)

    class Meta:
        verbose_name = _("Company")
        verbose_name_plural = _("Companies")

    @memoized_property
    def contacts(self):
        return Contact.objects. \
            filter(id_object=self.pk). \
            filter(model_type=CONTACT_MODEL_COMPANY). \
            all()

    def to_dict(self):
        return {
            'id': self.pk,
            'name': self.name,
            'unp': self.unp
        }
