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
        return super(TagViewset, self).list(request, *args,** kwargs)

    def create(self, request, *args, **kwargs):
        return super(TagViewset, self).create(request, *args,** kwargs)

    def retrieve(self, request, pk=None, *args, **kwargs):
        return super(TagViewset, self).retrieve(request, pk, *args,** kwargs)

    def update(self, request, pk=None, *args, **kwargs):
        return super(TagViewset, self).update(request, pk, *args,** kwargs)

    def partial_update(self, request, pk=None, *args, **kwargs):
        return super(TagViewset, self).partial_update(request, pk, *args,** kwargs)

    def destroy(self, request, pk=None, *args, **kwargs):
        return super(TagViewset, self).destroy(request, pk, *args,** kwargs)

    def get_queryset(self):
        queryset = Tag.objects.all()
        return queryset


class HostViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = Host.objects.filter(is_archive=False)
    serializer_class = HostSerializer
    filter_backends = (filter_rest_framework.DjangoFilterBackend, )
    filter_fields = ('name', )

    def list(self, request, *args, **kwargs):
        return super(HostViewset, self).list(request, *args,** kwargs)

    def create(self, request, *args, **kwargs):
        return super(HostViewset, self).create(request, *args,** kwargs)

    def retrieve(self, request, pk=None, *args, **kwargs):
        return super(HostViewset, self).retrieve(request, pk, *args,** kwargs)

    def update(self, request, pk=None, *args, **kwargs):
        return super(HostViewset, self).update(request, pk, *args,** kwargs)

    def partial_update(self, request, pk=None, *args, **kwargs):
        return super(HostViewset, self).partial_update(request, pk, *args,** kwargs)

    def destroy(self, request, pk=None, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.archive()
        except Http404:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)


class EventViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = Event.objects.filter(is_archive=False)
    serializer_class = EventSerializer

    def list(self, request, *args, **kwargs):
        return super(EventViewset, self).list(request, *args,** kwargs)

    def create(self, request, *args, **kwargs):
        return super(EventViewset, self).create(request, *args,** kwargs)

    def retrieve(self, request, pk=None, *args, **kwargs):
        return super(EventViewset, self).retrieve(request, pk, *args,** kwargs)

    def update(self, request, pk=None, *args, **kwargs):
        return super(EventViewset, self).update(request, pk, *args,** kwargs)

    def partial_update(self, request, pk=None, *args, **kwargs):
        return super(EventViewset, self).partial_update(request, pk, *args,** kwargs)

    def destroy(self, request, pk=None, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.archive()
        except Http404:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)


class SubscriberViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    serializer_class = SubscriberSerializer

    def get_queryset(self):
        event_pk = self.kwargs['event_pk']
        queryset = Subscriber.objects.none()
        if event_pk:
            queryset = Subscriber.objects.filter(event=event_pk, is_archive = False)
        return queryset

    def list(self, request, event_pk=None, *args, **kwargs):
        return super(SubscriberViewset, self).list(request, *args,** kwargs)

    def retrieve(self, request, pk=None, event_pk=None, *args, **kwargs):
        return super(SubscriberViewset, self).retrieve(request, *args,** kwargs)

    def create(self, request, event_pk=None, *args, **kwargs):
        return super(SubscriberViewset, self).create(request, *args,** kwargs)

    def update(self, request, event_pk=None, pk=None, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def partial_update(self, request, event_pk=None, pk=None, *args, **kwargs):
        return super(SubscriberViewset, self).partial_update(request, pk, *args,** kwargs)

    def destroy(self, request, event_pk=None, pk=None, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.archive()
        except Http404:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)