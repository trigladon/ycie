from django.db import models
from django.utils import timezone
from django.conf import settings

from django.utils.translation import ugettext_lazy as _


__all__ = (
    'Voting',
    'VotingOption'
)


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
