from django.db import models
from .utils import uuid4_hash_generator


DEVICES = (
    ('desktop', 'Desktop'),
    ('tablet', 'Tablet'),
    ('mobile', 'Mobile'),
)


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class DeviceUrl(BaseModel):
    type = models.CharField(choices=DEVICES, max_length=10)
    url = models.ForeignKey('ShortUrl', related_name='device_urls')
    target = models.URLField()
    counter = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ('type', 'url')

from django.db.utils import IntegrityError
class ShortUrl(BaseModel):
    hash = models.CharField(unique=True, default=uuid4_hash_generator, editable=False, max_length=8)
    target = models.URLField(unique=True)
    counter = models.PositiveIntegerField(default=0)

    @property
    def mobile_url(self):
        return self.get_device_url('mobile')

    @mobile_url.setter
    def mobile_url(self, value):
        self.set_device_url('mobile', value)

    @property
    def tablet_url(self):
        return self.get_device_url('tablet')

    @tablet_url.setter
    def tablet_url(self, value):
        self.set_device_url('tablet', value)

    @property
    def desktop_url(self):
        return self.get_device_url('desktop')

    @desktop_url.setter
    def desktop_url(self, value):
        self.set_device_url('desktop', value)

    def set_device_url(self, type, value):
        device_url = self.get_device_url(type=type)
        if device_url:
            device_url.target = value
            device_url.save()
        else:
            DeviceUrl.objects.create(url=self, type=type, target=value)

    def get_device_url(self, type):
        return self.device_urls.filter(type=type).first()

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        try:
            super().save(force_insert, force_update, using, update_fields)
        except IntegrityError as e:
            id = uuid4_hash_generator()
            self.save()