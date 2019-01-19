from rest_framework import serializers, validators
from django.db.models import Q
from .models import Tag, Host, Event, Subscriber
from hsc_backend._base.constants import SubscriberChoice
import json
# Serializers go here


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('pk', 'name')


class HostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Host
        fields = ('pk', 'name', 'url', 'description')


class EventSerializer(serializers.ModelSerializer):
    host = HostSerializer(read_only = True)

    def create(self, validated_data):
        event = Event.objects.create(**validated_data)
        if 'image' in self.context['request'].data:
            event.image = self.context['request'].data['image']
        
        event_data = json.loads(self.context['request'].data['event'])
        host = None
        if 'host' in event_data:
            host_id = event_data['host']
            host = Host.objects.filter(id=host_id, is_archive=False).first()
        event.host = host
            
        event.save()

        return event

    def update(self, instance, validated_data):
        instance = super(EventSerializer, self).update(
            instance, validated_data)

        if 'image' in self.context['request'].data:
            instance.image = self.context['request'].data['image']
        
        event_data = json.loads(self.context['request'].data['event'])
        if 'host' in event_data:
            host_id = event_data['host']
            host = Host.objects.filter(id=host_id, is_archive=False).first()
            instance.host = host

        instance.save()
        return instance

    class Meta:
        model = Event
        fields = (
            'pk', 'name', 'description', 'date',
            'host', 'image', 'short_description'
        )


class SubscriberSerializer(serializers.ModelSerializer):

    first_name = serializers.CharField(max_length=50, required=True)
    last_name = serializers.CharField(max_length=50, default="")
    gender = serializers.ChoiceField(
        choices=SubscriberChoice.GENDER_CHOICES, default="O")
    status = serializers.ChoiceField(
        choices=SubscriberChoice.SUBSCRIBER_STATUS_CHOICES, default="P")

    def validate_email(self, email):
        if email:
            event = self.context['view'].kwargs['event_pk']
            queryset = Subscriber.objects.filter(event_id=event, email=email)
            if queryset:
                raise serializers.ValidationError("This email is already used")
            else:
                return email

    def validate_phone(self, phone):
        if phone:
            event = self.context['view'].kwargs['event_pk']
            queryset = Subscriber.objects.filter(event_id=event, phone=phone)
            if queryset:
                raise serializers.ValidationError(
                    "This phone number is already used")
            else:
                return phone

    def create(self, validated_data):
        event = Event.objects.filter(
            id=self.context['view'].kwargs['event_pk']
        ).first()
        validated_data['event'] = event
        return Subscriber.objects.create(**validated_data)

    class Meta:
        model = Subscriber
        fields = (
            'pk', 'first_name', 'last_name', 'email', 'phone',
            'event', 'gender', 'status', 'birthday', 'address'
        )
