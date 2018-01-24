from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from house.models import House
from .helper import upload_file, get_storage_path
from .storage import get_file_storage
from .constants import *


class Asset(models.Model):
    """
    Files model
    """
    ASSET_TYPES = (
        (ASSET_TYPE_CATEGORY_NEWS, _('Category news')),
        (ASSET_TYPE_NEWS, _('News'))
    )

    title = models.CharField(verbose_name=_("Title"), max_length=511, blank=True, null=True)
    file = models.FileField(verbose_name=_("File"), upload_to=upload_file, null=False, blank=False, storage=get_file_storage())
    file_real_name = models.TextField(_("Real file name"), null=False, blank=False)
    is_published = models.BooleanField(_("Is published"), null=False, blank=False)
    type = models.CharField(_("Model type"), choices=ASSET_TYPES, default=ASSET_TYPE_NEWS, max_length=15, null=True, blank=True)
    updated_date = models.DateTimeField(_("updated date"), default=timezone.now)
    created_date = models.DateTimeField(_("created date"), default=timezone.now, editable=False)

    class Meta:
        verbose_name = _("Asset")
        verbose_name_plural = _("Assets")


class Country(models.Model):
    """
    Country model
    """
    name = models.CharField(_('Name'), max_length=150, null=False, blank=False)
    english_name = models.CharField(_('English Name'), max_length=150, null=False, blank=False)
    short_name = models.CharField(_('Short name'), max_length=50, null=False, blank=False)
    is_published = models.BooleanField(_('Is published'), default=False)

    class Meta:
        verbose_name = _("Country")
        verbose_name_plural = _("Countries")

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

    class Meta:
        verbose_name = _("City")
        verbose_name_plural = _("Cities")

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
    create_date = models.DateTimeField(_('Create date'), default=timezone.now, editable=False)

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


class CategoryNews(models.Model):
    house = models.ForeignKey(House, verbose_name=_('House'), null=True, on_delete=models.CASCADE)
    title = models.CharField(verbose_name=_('Title'), null=False, max_length=1023)
    shot_description = models.TextField(verbose_name=_('Shot description'), null=True)
    description = models.TextField(verbose_name=_('Description'), null=True)
    is_published = models.BooleanField(verbose_name=_('Is published?'), default=True)
    update_date = models.DateTimeField(_('Update date'), default=timezone.now, editable=False)
    create_date = models.DateTimeField(_('Create date'), default=timezone.now, editable=False)

    class Meta:
        verbose_name = _("CategoryNews")
        verbose_name_plural = _("CategoriesNews")

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.pk:
            self.update_date = timezone.now()
        return super(CategoryNews, self).save(force_insert=force_insert, force_update=force_update, using=using,
                                              update_fields=update_fields)


class News(models.Model):
    pass


class Voting(models.Model):
    pass