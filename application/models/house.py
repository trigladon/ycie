from django.db import models
from django.conf import settings
from django.utils import timezone

from django.utils.translation import ugettext_lazy as _

from .company import Company
from ..constants import (
    GOVERNMENT_ROLE_ADMIN,
    GOVERNMENT_ROLE_MANAGER
)

__all__ = (
    'House',
    'Government',
    'GovernmentUser'
)


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





