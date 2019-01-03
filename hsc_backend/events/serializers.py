from rest_framework import serializers
from .models import Tag, Host, Event, Subscriber
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

    def create(self, validated_data):
        event = Event.objects.create(**validated_data)

        return event

    class Meta:
        model = Event
        fields = (
            'pk', 'name', 'description', 'date',
            'host',
        )


class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = (
            'first_name', 'last_name', 'email', 'phone'
        )
