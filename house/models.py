from django.db import models
from django.conf import settings
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from account.models import Company
from .constants import *


class House(models.Model):
    """
    House model
    """
    company = models.ForeignKey(Company, null=True, on_delete=models.SET_NULL, verbose_name=_('Company'))
    address = models.CharField(_('Address'), null=False, blank=False, max_length=511)
    is_multi_apartments = models.BooleanField(_('Is multi apartments?'), default=False)
    update_date = models.DateTimeField(_('Update date'), default=timezone.now, editable=False)
    create_date = models.DateTimeField(_('Create date'), default=timezone.now, editable=False)

    class Meta:
        verbose_name = _("House")
        verbose_name_plural = _("Houses")

    def to_dict(self):
        return {
            'id': self.pk,
            'address': self.address,
            'is_multi_apartments': self.is_multi_apartments
        }


class Government(models.Model):
    """
    Government model
    """
    company = models.ForeignKey(Company, null=True, on_delete=models.SET_NULL)
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, through='GovernmentUser')

    class Meta:
        verbose_name = _("Government")
        verbose_name_plural = _("Governments")

    def to_dict(self):
        return {
            'id': self.pk,
            'company': self.company
        }


class GovernmentUser(models.Model):
    """
    Through model Government User
    """
    MODEL_ROLES = (
        (GOVERNMENT_ROLE_ADMIN, _('Admin')),
        (GOVERNMENT_ROLE_MANAGER, _('Manager'))
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_('User'), on_delete=models.CASCADE)
    government = models.ForeignKey(Government, verbose_name=_('Government'), on_delete=models.CASCADE)
    role = models.CharField(_('Role'), choices=MODEL_ROLES, default=GOVERNMENT_ROLE_MANAGER, null=False, max_length=15)
    date_joined = models.DateTimeField(_('Date joined '), default=timezone.now, editable=False)

    def to_dict(self):
        return {
            'id': self.pk,
            'user_id': self.user_id,
            'government_id': self.government_id,
            'role': self.role,
            'date_joined': self.date_joined
        }


class Apartment(models.Model):
    """
    Apartment model
    """
    house = models.ForeignKey(House, verbose_name=_('House id'), null=True, on_delete=models.SET_NULL)
    number = models.IntegerField(_('Number'), null=False, blank=False)
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, through='ApartmentUser')
    update_date = models.DateTimeField(_('Update date'), default=timezone.now, editable=False)
    create_date = models.DateTimeField(_('Create date'), default=timezone.now, editable=False)

    class Meta:
        verbose_name = _("Apartment")
        verbose_name_plural = _("Apartments")

    def to_dict(self):
        return {
            'id': self.pk,
            'house': self.house,
            'number': self.number,
        }


class ApartmentUser(models.Model):
    """
    Through model Apartment User
    """
    MODEL_ROLES = (
        (APARTMENT_ROLE_TENANT, _('Tenant')),
        (APARTMENT_ROLE_OWNER, _('Owner')),
        (APARTMENT_ROLE_LODGER, _('Lodger')),
    )

    APARTMENT_STATUS = (
        (APARTMENT_STATUS_UNDER_CONSIDERATION_GOVERNMENT, _('Under consideration in a government')),
        (APARTMENT_STATUS_UNDER_CONSIDERATION_HOUSE, _('Under consideration in a house owner')),
        (APARTMENT_STATUS_BLOCKED, _('Blocked')),
        (APARTMENT_STATUS_BLOCKED, _('Accepted')),
    )

    apartment = models.ForeignKey(Apartment, verbose_name=_('Apartment'), null=False, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_('User'), null=False, on_delete=models.CASCADE)
    role = models.CharField(_('Role'), choices=MODEL_ROLES, default=APARTMENT_ROLE_LODGER, null=False, max_length=15)
    status = models.CharField(_('Status'), choices=APARTMENT_STATUS,
                              default=APARTMENT_STATUS_UNDER_CONSIDERATION_GOVERNMENT, null=False, max_length=55),
    date_joined = models.DateTimeField(_('Date joined '), default=timezone.now, editable=False)

    def to_dict(self):
        return {
            'id': self.pk,
            'user_id': self.user_id,
            'apartment_id': self.apartment_id,
            'role': self.role,
            'date_joined': self.date_joined
        }


