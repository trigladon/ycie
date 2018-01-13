from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from .constants import *


class Country(models.Model):
    """
    Country model
    """
    name = models.CharField(_('Name'), max_length=150, null=False, blank=False)
    english_name = models.CharField(_('English Name'), max_length=150, null=False, blank=False)
    short_name = models.CharField(_('Short name'), max_length=50, null=False, blank=False)
    is_published = models.BooleanField(_('Is published'), default=False)

    def to_dict(self):
        return {
            'id': self.pk,
            'name': self.name,
            'english_name': self.english_name,
            'short_name': self.short_name,
            'is_published': self.is_published
        }


class City(models.Model):
    """
    City model
    """
    country_id = models.ForeignKey(Country, blank=False, null=False, on_delete=models.CASCADE, verbose_name=_('County id'))
    name = models.CharField(_('City name'), null=False, blank=False, max_length=150)
    english_name = models.CharField(_('English Name'), max_length=150, null=False, blank=False)
    short_name = models.CharField(_('Short name'), max_length=50, null=False, blank=False)
    is_published = models.BooleanField(_('Is published'), default=False)

    def to_dict(self):
        return {
            'id': self.pk,
            'country_id': self.country_id,
            'name': self.name,
            'english_name': self.english_name,
            'short_name': self.short_name,
            'is_published': self.is_published
        }


class Contact(models.Model):
    """
    Contact model for users and companies 
    """
    TYPES = (
        (CONTACT_TYPE_EMAIL, _('Email')),
        (CONTACT_TYPE_FAX, _('Fax')),
        (CONTACT_TYPE_ZIP, _('Zip')),
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
    city_id = models.ForeignKey(City, null=True, blank=True, on_delete=models.SET_NULL)
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
