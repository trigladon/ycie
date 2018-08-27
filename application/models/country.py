from django.db import models
from django.utils.translation import ugettext_lazy as _


__all__ = (
    'Country',
    'City'
)


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
