from rest_framework_nested import routers
from django.conf.urls import url, include
from .views import TagViewset, HostViewset, EventViewset, SubscriberViewset

router = routers.DefaultRouter()
router.register(r'tags', TagViewset, base_name='tags')
router.register(r'hosts', HostViewset, base_name='hosts')
router.register(r'events', EventViewset, base_name='events')

subscriber_router = routers.NestedDefaultRouter(router, r'events', lookup='event')
subscriber_router.register(r'subscribers', SubscriberViewset, base_name='event_subscribers')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^', include(subscriber_router.urls)),
]