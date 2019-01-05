from rest_framework_nested import routers
from django.conf.urls import url, include, re_path
from .views import TagViewset, HostViewset, EventViewset, SubscriberViewset

router = routers.DefaultRouter()
router.register(r'tags', TagViewset, base_name='tags')
router.register(r'hosts', HostViewset, base_name='hosts')

router.register(r'events', EventViewset, base_name='events')
subscriber_router = routers.NestedDefaultRouter(router, r'events', lookup='event')
subscriber_router.register(r'subscribers', SubscriberViewset, base_name='event_subscribers')

app_name="events"

urlpatterns = [
    re_path(r'^', include(router.urls)),
    re_path(r'^', include(subscriber_router.urls))
]