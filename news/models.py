from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from house.models import House


class Category(models.Model):
    """
    Model for news category
    """
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
        return super(Category, self).save(force_insert=force_insert, force_update=force_update, using=using,
                                          update_fields=update_fields)


class News(models.Model):
    """
    Model for news
    """
    category = models.ForeignKey(Category, null=True, default=None, verbose_name=_('Category'),
                                 on_delete=models.CASCADE)
    title = models.CharField(verbose_name=_('Title'), null=False, max_length=1023)
    shot_description = models.TextField(verbose_name=_('Shot description'), null=True)
    description = models.TextField(verbose_name=_('Description'), null=True)
    is_published = models.BooleanField(verbose_name=_('Is published?'), default=True)
    update_date = models.DateTimeField(_('Update date'), default=timezone.now, editable=False)
    create_date = models.DateTimeField(_('Create date'), default=timezone.now, editable=False)

    class Meta:
        verbose_name = _("News")
        verbose_name_plural = _("News")

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.pk:
            self.update_date = timezone.now()
        return super(News, self).save(force_insert=force_insert, force_update=force_update, using=using,
                                      update_fields=update_fields)