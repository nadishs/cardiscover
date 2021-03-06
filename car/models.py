from django.core.urlresolvers import reverse
from django.db.models import *
from django_extensions.db.fields import AutoSlugField
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import models as auth_models
from django.db import models as models
from django_extensions.db import fields as extension_fields


class carName(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    Manufacturer = models.TextField(max_length=100)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    mileage = models.DecimalField(max_digits=10, decimal_places=2)
    engine = models.DecimalField(max_digits=10, decimal_places=2)
    power = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(max_length=1000)
    fueltype = models.CharField(max_length=10)
    bodytype = models.CharField(max_length=10)
    cardheko = models.CharField(max_length=100)
    cartrade = models.CharField(max_length=100)
    youtubeurl = models.CharField(max_length=50)
    imageUrl = models.CharField(max_length=150)


    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('car_carname_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('car_carname_update', args=(self.slug,))


class Manufacturer(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)


    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('car_manufacturer_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('car_manufacturer_update', args=(self.slug,))


