from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from hsc_backend._base.models import BaseModel
from hsc_backend._base.constants import SubscriberChoice
# Create your models here.


class Subscriber(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = PhoneNumberField()
    gender = models.CharField(
        max_length=1, choices=SubscriberChoice.GENDER_CHOICES,
        null=True,
        default='O'
    )
    birthday = models.DateField(null=True, blank=False)
    event = models.ForeignKey(
        'Event', on_delete=models.DO_NOTHING, null=True, blank=False)
    status = models.CharField(
        max_length=1, choices=SubscriberChoice.SUBSCRIBER_STATUS_CHOICES,
        null=True,
        default='P'
    )
    is_archive = models.BooleanField(default=False, null= True, blank=False)
    
    address = models.CharField(max_length=250, null=True, blank=False)


    def __str__(self):
        return ("%s %s" % (self.first_name, self.last_name))


class Host(BaseModel):
    name = models.CharField(max_length=255)
    url = models.URLField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Event(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    date = models.DateTimeField()
    host = models.ForeignKey(
        Host, null=True, blank=True, on_delete=models.SET_NULL)
    tags = models.ManyToManyField(
        Tag, through='EventTag', related_name='tags_set')
    image = models.ImageField(upload_to='events/%Y/%m/', null=True)
    short_description = models.CharField(null=True, blank=True, max_length=255)

    def __str__(self):
        return self.name


class EventTag(models.Model):
    event = models.ForeignKey(Event, on_delete=models.DO_NOTHING)
    tag = models.ForeignKey(Tag, on_delete=models.DO_NOTHING)
