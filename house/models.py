from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from account.models import User, Role, Company


class House(models.Model):
    address = models.CharField(_('Address'), null=False, blank=False)
    update_date = models.DateTimeField(_('Update date'), default=timezone.now, editable=False)
    create_date = models.DateTimeField(_('Create date'), default=timezone.now, editable=False)


class Government(models.Model):
    company = models.ForeignKey(Company, null=True, on_delete=models.SET_NULL)
    users = models.ManyToManyField(User, through='')


class Apartment(models.Model):
    house_id = models.ForeignKey(House, verbose_name=_('House id'), null=True, on_delete=models.SET_NULL)
    number = models.IntegerField(_('Number'), null=False, blank=False)
    update_date = models.DateTimeField(_('Update date'), default=timezone.now, editable=False)
    create_date = models.DateTimeField(_('Create date'), default=timezone.now, editable=False)
