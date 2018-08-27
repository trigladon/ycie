from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

__all__ = (
    'Company',
)


class Company(models.Model):
    """
    Company model
    """
    name = models.CharField(_('Organization name'), max_length=511, null=False)
    unp = models.CharField(_('UNP'), max_length=15, null=False)
    email = models.EmailField(_('Email address'), blank=False, unique=True, null=False)
    phone_number = models.CharField(_('Phone number'), blank=False, null=False, max_length=12)
    legal_address = models.CharField(_('Legal address'), null=True, blank=True, max_length=1023)
    physical_address = models.CharField(_('Physical address'), null=True, blank=True, max_length=1023)
    zip = models.IntegerField(_('Zip code'), null=True, blank=True)
    city_id = models.ForeignKey('City', verbose_name=_('City'), null=True, blank=False, on_delete=models.SET_NULL)
    update_date = models.DateTimeField(_('Update date'), default=timezone.now, editable=False)
    create_date = models.DateTimeField(_('Create date'), default=timezone.now, editable=False)

    class Meta:
        verbose_name = _("Company")
        verbose_name_plural = _("Companies")

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.pk:
            self.update_date = timezone.now()
        return super(Company, self).save(force_insert=force_insert, force_update=force_update, using=using,
                                         update_fields=update_fields)

    def to_dict(self):
        return {
            'id': self.pk,
            'name': self.name,
            'unp': self.unp,
            'city_id': self.city_id
        }