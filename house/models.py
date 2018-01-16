from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from account.models import User, Company
from .constants import *


class House(models.Model):
    """
    House model
    """
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


class Role(models.Model):
    """
    Role model
    """
    MODEL_ROLES = (
        (ROLE_ADMIN, _('Admin')),
        (ROLE_MANAGER, _('Manager'))
    )

    name = models.CharField(_('Name'), choices=MODEL_ROLES, max_length=15, null=False)
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
    user = models.ForeignKey(User, verbose_name=_('User'), on_delete=models.CASCADE)
    government = models.ForeignKey(Government, verbose_name=_('Government'), on_delete=models.CASCADE)
    role = models.CharField(_('Role'), default=ROLE_MANAGER, null=False, max_length=15)
    date_joined = models.DateTimeField(_('Date joined '), default=timezone.now, editable=False)


class Apartment(models.Model):
    """
    Apartment model
    """
    house = models.ForeignKey(House, verbose_name=_('House id'), null=True, on_delete=models.SET_NULL)
    number = models.IntegerField(_('Number'), null=False, blank=False)
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
