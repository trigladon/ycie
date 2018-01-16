from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser

from memoized_property import memoized_property

from application.constants import CONTACT_MODEL_USER, CONTACT_MODEL_COMPANY
from application.models import Contact, City
from .manager import UserManager


class User(AbstractUser):
    """
    User model    
    """
    username = models.CharField(_('username'), max_length=150, unique=False, blank=True, null=True)
    email = models.EmailField(_('email address'), blank=False, unique=True, null=False)

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'

    @memoized_property
    def contacts(self):
        return Contact.objects. \
            filter(id_object=self.pk). \
            filter(model_type=CONTACT_MODEL_USER). \
            all()

    def to_dict(self):
        return {
            'id': self.pk,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'is_active': self.is_active,
            'is_staff': self.is_staff,
            'date_joined': self.date_joined
        }


class Company(models.Model):
    """
    Company model
    """
    name = models.CharField(_('Organization name'), max_length=511, null=False)
    unp = models.CharField(_('UNP'), max_length=15, null=False)
    city_id = models.ForeignKey(City, verbose_name=_('City'), null=True, blank=False, on_delete=models.SET_NULL)
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

    @memoized_property
    def contacts(self):
        return Contact.objects. \
            filter(id_object=self.pk). \
            filter(model_type=CONTACT_MODEL_COMPANY). \
            all()

    def to_dict(self):
        return {
            'id': self.pk,
            'name': self.name,
            'unp': self.unp,
            'city_id': self.city_id
        }
