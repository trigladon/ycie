from django.db import models
from django.utils import timezone

from django.utils.translation import ugettext_lazy as _

from ..managers import NewsCategoryManager, NewsAssetManager
from application.storage.helper import upload_file
from ..storage import get_file_storage
from ..constants import *


__all__ = (
    'Asset',
    'NewsAsset',
    'NewsCategoryAsset'
)


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
