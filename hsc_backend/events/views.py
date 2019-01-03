from django.shortcuts import render
from django.http import Http404
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filter_rest_framework
from .models import Tag, Host, Event, Subscriber
from .serializers import TagSerializer, HostSerializer, EventSerializer, SubscriberSerializer

# Create your views here.


class TagViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    serializer_class = TagSerializer

    def list(self, request, *args, **kwargs):
        return super(TagViewset, self).list(request, args, kwargs)

    def create(self, request, *args, **kwargs):
        return super(TagViewset, self).create(request, args, kwargs)

    def retrieve(self, request, pk=None, *args, **kwargs):
        return super(TagViewset, self).retrieve(request, pk, args, kwargs)

    def update(self, request, pk=None, *args, **kwargs):
        return super(TagViewset, self).update(request, pk, args, kwargs)

    def partial_update(self, request, pk=None, *args, **kwargs):
        return super(TagViewset, self).partial_update(request, pk, args, kwargs)

    def destroy(self, request, pk=None, *args, **kwargs):
        return super(TagViewset, self).destroy(request, pk, args, kwargs)

    def get_queryset(self):
        queryset = Tag.objects.all()
        return queryset


class HostViewset(viewsets.ModelViewSet):
    queryset = Host.objects.all()
    serializer_class = HostSerializer
    filter_backends = (filter_rest_framework.DjangoFilterBackend, )
    filter_fields = ('name', )

    def list(self, request, *args, **kwargs):
        return super(HostViewset, self).list(request, args, kwargs)

    def create(self, request, *args, **kwargs):
        return super(HostViewset, self).create(request, args, kwargs)

    def retrieve(self, request, pk=None, *args, **kwargs):
        return super(HostViewset, self).retrieve(request, pk, args, kwargs)

    def update(self, request, pk=None, *args, **kwargs):
        return super(HostViewset, self).update(request, pk, args, kwargs)

    def partial_update(self, request, pk=None, *args, **kwargs):
        return super(HostViewset, self).partial_update(request, pk, args, kwargs)

    def destroy(self, request, pk=None, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.archive()
        except Http404:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)


class EventViewset(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def list(self, request, *args, **kwargs):
        return super(EventViewset, self).list(request, args, kwargs)

    def create(self, request, *args, **kwargs):
        return super(EventViewset, self).create(request, args, kwargs)

    def retrieve(self, request, pk=None, *args, **kwargs):
        return super(EventViewset, self).retrieve(request, pk, args, kwargs)

    def update(self, request, pk=None, *args, **kwargs):
        return super(EventViewset, self).update(request, pk, args, kwargs)

    def partial_update(self, request, pk=None, *args, **kwargs):
        return super(EventViewset, self).partial_update(request, pk, args, kwargs)

    def destroy(self, request, pk=None, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.archive()
        except Http404:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class SubscriberViewset(viewsets.ModelViewSet):
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer

    def list(self, request, event_pk=None):
        queryset = self.queryset.filter(event = event_pk)
        serializer = SubscriberSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, event_pk=None):
        queryset = self.queryset.get(pk=pk, event=event_pk)
        serializer = SubscriberSerializer(queryset)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        return super(SubscriberViewset, self).create(request, args, kwargs)


    def update(self, request, pk=None, *args, **kwargs):
        return super(SubscriberViewset, self).update(request, pk, args, kwargs)

    def partial_update(self, request, pk=None, *args, **kwargs):
        return super(SubscriberViewset, self).partial_update(request, pk, args, kwargs)

    def destroy(self, request, pk=None, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.archive()
        except Http404:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)