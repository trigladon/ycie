from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from memoized_property import memoized_property

from .manager import NewsCategoryManager, NewsAssetManager
from .helper import upload_file
from .storage import get_file_storage
from .constants import *

from .manager import UserManager
from .constants import \
    CONTACT_TYPE_EMAIL, \
    CONTACT_TYPE_FAX, \
    CONTACT_TYPE_ZIP, \
    CONTACT_TYPE_LEGAL_ADDRESS, \
    CONTACT_TYPE_PHYSICAL_ADDRESS, \
    CONTACT_MODEL_USER, \
    CONTACT_MODEL_COMPANY


class Contact(models.Model):
    """
    Contact model for users and companies
    """
    TYPES = (
        (CONTACT_TYPE_EMAIL, _('Email')),
        (CONTACT_TYPE_FAX, _('Fax')),
        (CONTACT_TYPE_ZIP, _('Zip')),
        (CONTACT_TYPE_LEGAL_ADDRESS, _('Legal address')),
        (CONTACT_TYPE_PHYSICAL_ADDRESS, _('Physical address')),
    )

    MODEL_TYPES = (
        (CONTACT_MODEL_COMPANY, _('Company')),
        (CONTACT_MODEL_USER, _('User'))
    )

    id_object = models.IntegerField(_('Id object'), blank=False, null=False)
    type = models.CharField(_('Type'), choices=TYPES, null=False, max_length=20)
    model = models.CharField(_('Model'), choices=MODEL_TYPES, null=False, max_length=20)
    data = models.CharField(_('Data'), null=False, max_length=1023)
    city_id = models.ForeignKey('City', null=True, blank=True, on_delete=models.SET_NULL)
    create_date = models.DateTimeField(_('Create date'), default=timezone.now, editable=False)

    class Meta:
        verbose_name = _("Contact")
        verbose_name_plural = _("Contacts")

    def to_dict(self):
        return {
            'id': self.pk,
            'id_object': self.id_object,
            'type': self.type,
            'model': self.model,
            'data': self.data,
            'create_date': self.create_date
        }


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


class House(models.Model):
    """
    House model
    """
    company = models.ForeignKey(Company, null=True, on_delete=models.SET_NULL, verbose_name=_('Company'))
    address = models.CharField(_('Address'), null=False, blank=False, max_length=511)
    is_multi_apartments = models.BooleanField(_('Is multi apartments?'), default=False)
    update_date = models.DateTimeField(_('Update date'), default=timezone.now, editable=False)
    create_date = models.DateTimeField(_('Create date'), default=timezone.now, editable=False)

    class Meta:
        verbose_name = _("House")
        verbose_name_plural = _("Houses")

    def to_dict(self):
        return {
            'id': self.pk,
            'address': self.address,
            'is_multi_apartments': self.is_multi_apartments
        }


class Government(models.Model):
    """
    Government model
    """
    company = models.ForeignKey(Company, null=True, on_delete=models.SET_NULL)
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, through='GovernmentUser')

    class Meta:
        verbose_name = _("Government")
        verbose_name_plural = _("Governments")

    def to_dict(self):
        return {
            'id': self.pk,
            'company': self.company
        }


class GovernmentUser(models.Model):
    """
    Through model Government User
    """
    MODEL_ROLES = (
        (GOVERNMENT_ROLE_ADMIN, _('Admin')),
        (GOVERNMENT_ROLE_MANAGER, _('Manager'))
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_('User'), on_delete=models.CASCADE)
    government = models.ForeignKey(Government, verbose_name=_('Government'), on_delete=models.CASCADE)
    role = models.CharField(_('Role'), choices=MODEL_ROLES, default=GOVERNMENT_ROLE_MANAGER, null=False, max_length=15)
    date_joined = models.DateTimeField(_('Date joined '), default=timezone.now, editable=False)

    def to_dict(self):
        return {
            'id': self.pk,
            'user_id': self.user_id,
            'government_id': self.government_id,
            'role': self.role,
            'date_joined': self.date_joined
        }


class Apartment(models.Model):
    """
    Apartment model
    """
    house = models.ForeignKey(House, verbose_name=_('House id'), null=True, on_delete=models.SET_NULL)
    number = models.IntegerField(_('Number'), null=False, blank=False)
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, through='ApartmentUser')
    update_date = models.DateTimeField(_('Update date'), default=timezone.now, editable=False)
    create_date = models.DateTimeField(_('Create date'), default=timezone.now, editable=False)

    class Meta:
        verbose_name = _("Apartment")
        verbose_name_plural = _("Apartments")

    def to_dict(self):
        return {
            'id': self.pk,
            'house': self.house,
            'number': self.number,
        }


class ApartmentUser(models.Model):
    """
    Through model Apartment User
    """
    apartment = models.ForeignKey(Apartment, verbose_name=_('Apartment'), null=False, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_('User'), null=False, on_delete=models.CASCADE)
    role = models.CharField(_('Role'), choices=MODEL_ROLES, default=APARTMENT_ROLE_LODGER, null=False, max_length=15)
    status = models.CharField(_('Status'), choices=APARTMENT_STATUS,
                              default=APARTMENT_STATUS_UNDER_CONSIDERATION_GOVERNMENT, null=False, max_length=55),
    date_joined = models.DateTimeField(_('Date joined '), default=timezone.now, editable=False)

    def to_dict(self):
        return {
            'id': self.pk,
            'user_id': self.user_id,
            'apartment_id': self.apartment_id,
            'role': self.role,
            'date_joined': self.date_joined
        }


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
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

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