from django.db import models
from django.utils import timezone
from django.conf import settings

from django.utils.translation import ugettext_lazy as _

from .house import House
from ..constants import (
    MODEL_ROLES,
    APARTMENT_ROLE_LODGER,
    APARTMENT_STATUS,
    APARTMENT_STATUS_UNDER_CONSIDERATION_GOVERNMENT
)

__all__ = (
    'Apartment',
    'ApartmentUser'
)


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
