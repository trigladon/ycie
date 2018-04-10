from django.db import models
from django.utils import timezone
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from .manager import NewsCategoryManager, NewsAssetManager
from .helper import upload_file
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
    file = models.FileField(verbose_name=_("File"), upload_to=upload_file, null=False, blank=False,
                            storage=get_file_storage())
    file_real_name = models.TextField(_("Real file name"), null=False, blank=False)
    is_published = models.BooleanField(_("Is published"), null=False, blank=False)
    type = models.CharField(_("Type"), choices=ASSET_TYPES, default=ASSET_TYPE_NEWS, max_length=15, null=True,
                            blank=True)
    updated_date = models.DateTimeField(_("updated date"), default=timezone.now)
    created_date = models.DateTimeField(_("created date"), default=timezone.now, editable=False)

    class Meta:
        verbose_name = _("Asset")
        verbose_name_plural = _("Assets")

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'is_published': self.is_published,
            'type': self.type,
        }


class NewsAsset(Asset):
    objects = NewsAssetManager()

    class Meta:
        proxy = True


class NewsCategoryAsset(Asset):
    objects = NewsCategoryManager()

    class Meta:
        proxy = True


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
    country_id = models.ForeignKey(Country, blank=False, null=False, on_delete=models.CASCADE,
                                   verbose_name=_('County id'))
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


class Voting(models.Model):
    """
    Model for voting
    """
    title = models.CharField(verbose_name=_('Title'), null=False, max_length=1023)
    description = models.TextField(verbose_name=_('Description'), null=True)
    type = models.CharField(_('Type'), null=False, choices=(), max_length=50)
    update_date = models.DateTimeField(_('Update date'), default=timezone.now, editable=False)
    create_date = models.DateTimeField(_('Create date'), default=timezone.now, editable=False)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.pk:
            self.update_date = timezone.now()
        return super(Voting, self).save(force_insert=force_insert, force_update=force_update, using=using,
                                        update_fields=update_fields)

    def to_dict(self):
        return {

        }


class VotingOption(models.Model):
    """
    Options for voting
    """
    user = models.ManyToManyField(verbose_name=_('Users'), to=settings.AUTH_USER_MODEL)
    voting = models.ForeignKey(Voting, verbose_name=_('Voting'), null=False, on_delete=models.CASCADE)
    title = models.CharField(verbose_name=_('Title'), null=False, max_length=1023)
    description = models.CharField(verbose_name=_('Description'), null=False, max_length=1535)
    amount = models.IntegerField(verbose_name=_('Amount'), default=0, null=False)

    class Meta:
        verbose_name = _("VotingOptions")
        verbose_name_plural = _("VotingOptions")

    def to_dict(self):
        return {

        }
