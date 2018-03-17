# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from feder.institutions.models import Institution
from feder.records.models import AbstractRecord


class ParcelPostQuerySet(models.QuerySet):
    pass


class AbstractParcelPost(AbstractRecord):
    title = models.CharField(verbose_name=_("Title"), max_length=200)
    content = models.FileField(verbose_name=_("Content"))
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, help_text=_("Created by"))

    class Meta:
        abstract = True


class IncomingParcelPost(AbstractParcelPost):
    sender = models.ForeignKey(Institution, verbose_name=_("Sender"))
    comment = models.TextField(verbose_name=_("Comment"))
    receive_date = models.DateField(default=timezone.now, verbose_name=_("Receive date"))
    def get_absolute_url(self):
        return reverse('parcels:incoming-details', kwargs={'pk': str(self.pk)})

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = _("Incoming parcel post")
        verbose_name_plural = _("Incoming parcel posts")


class OutgoingParcelPost(AbstractParcelPost):
    recipient = models.ForeignKey(Institution, verbose_name=_("Recipient"))
    post_date = models.DateField(default=timezone.now, verbose_name=_("Post date"))

    def get_absolute_url(self):
        return reverse('parcels:outgoing-details', kwargs={'pk': str(self.pk)})

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = _("Outgoing parcel post")
        verbose_name_plural = _("Outgoing parcel posts")