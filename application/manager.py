from django.db.models import Manager
from django.contrib.auth.models import UserManager as DjUserManager

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


class UserManager(DjUserManager):

    def _create_user(self, username, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        # username = self.model.normalize_username(username)
        user = self.model(username=email, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        return super(UserManager, self).create_superuser(username=None, email=email, password=password, **extra_fields)

    def create_user(self, email, password=None, **extra_fields):
        return super(UserManager, self).create_user(username=None, email=email, password=password, **extra_fields)


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
