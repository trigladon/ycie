from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from account.models import User, Company
from .constants import *


class House(models.Model):
    """
    House model
    """
    company = models.ForeignKey(Company, null=True, on_delete=models.SET_NULL, verbose_name=_('Company'))
    address = models.CharField(_('Address'), null=False, blank=False, max_length=511)
    update_date = models.DateTimeField(_('Update date'), default=timezone.now, editable=False)
    create_date = models.DateTimeField(_('Create date'), default=timezone.now, editable=False)

    class Meta:
        verbose_name = _("House")
        verbose_name_plural = _("Houses")

    def to_dict(self):
        return {
            'id': self.pk,
            'address': self.address
        }


class Government(models.Model):
    """
    Government model
    """
    company = models.ForeignKey(Company, null=True, on_delete=models.SET_NULL)
    users = models.ManyToManyField(User, through='GovernmentUser')

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
        (ROLE_ADMIN, _('Admin')),
        (ROLE_MANAGER, _('Manager'))
    )

    user = models.ForeignKey(User, verbose_name=_('User'), on_delete=models.CASCADE)
    government = models.ForeignKey(Government, verbose_name=_('Government'), on_delete=models.CASCADE)
    role = models.CharField(_('Role'), choices=MODEL_ROLES, default=ROLE_MANAGER, null=False, max_length=15)
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
    users = models.ManyToManyField(User, through='ApartmentUser')
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

    apartment = models.ForeignKey(Apartment, verbose_name=_('Apartment'), null=False, on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name=_('User'), null=False, on_delete=models.CASCADE)
    role = models.CharField(_('Role'), choices=MODEL_ROLES, default=APARTMENT_ROLE_LODGER, null=False, max_length=15)
    date_joined = models.DateTimeField(_('Date joined '), default=timezone.now, editable=False)

    def to_dict(self):
        return {
            'id': self.pk,
            'user_id': self.user_id,
            'apartment_id': self.apartment_id,
            'role': self.role,
            'date_joined': self.date_joined
        }


