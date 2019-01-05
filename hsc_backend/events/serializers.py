from rest_framework import serializers, validators
from django.db.models import Q
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

    first_name = serializers.CharField(max_length=50, required=True)
    last_name = serializers.CharField(max_length=50, default="")
    gender = serializers.CharField(max_length=1, default="O")
    status = serializers.CharField(max_length=1, default="P")

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
            'event', 'gender', 'status', 'birthday'
        )
