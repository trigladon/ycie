from django.db.models import Manager

from ..constants import ASSET_TYPE_CATEGORY_NEWS


__all__ = (
    'NewsCategoryManager',
)


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