from django.db.models import Manager

from .constants import ASSET_TYPE_CATEGORY_NEWS, ASSET_TYPE_NEWS


class BaseAssetManager(Manager):
    """
    Base asset manager
    """
    def _get_by_type(self, asset_type):
        """
        :return:
        """
        return self.get_queryset().filer(type=asset_type)

    class Meta:
        abstract = True


class AssetManager(Manager):
    """
    Custom asset manager
    """
    use_for_related_fields = True


class NewsAssetManager(Manager):
    """
    News Asset manager
    """
    def get_queryset(self):
        """        
        :return: 
        """
        return super(NewsAssetManager, self).get_queryset().filter(type=ASSET_TYPE_NEWS)

    def create(self, **kwargs):
        """
        :param kwargs:
        :return:
        """
        kwargs.update({'type': ASSET_TYPE_NEWS})
        return super(NewsAssetManager, self).create(**kwargs)


class NewsCategoryManager(Manager):
    """
    News Category Asset manager
    """
    def get_queryset(self):
        """        
        :return: 
        """
        return super(NewsCategoryManager, self).get_queryset().filter(type=ASSET_TYPE_CATEGORY_NEWS)

    def create(self, **kwargs):
        """
        :param kwargs:
        :return:
        """
        kwargs.update({'type': ASSET_TYPE_CATEGORY_NEWS})
        return super(NewsCategoryManager, self).create(**kwargs)
