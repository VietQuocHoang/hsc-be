from rest_framework import routers
from django.conf.urls import url, include, re_path
from .views import UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, base_name='users')

app_name = "users"

urlpatterns = [
    re_path(r'^', include(router.urls))
]
