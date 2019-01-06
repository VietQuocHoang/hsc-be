from django.shortcuts import render
from django.http import Http404
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from django.contrib.auth.views import auth_login
from django.contrib.auth.models import User
from .serializers import UserSerializer
# Create your views here.

UserModel = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    serializer_class = UserSerializer
    http_method_names = ['get', 'post','head', 'patch']
    def list(self, request, *args, **kwargs):
        return super(UserViewSet, self).list(request, *args, ** kwargs)

    def create(self, request, *args, **kwargs):
        return super(UserViewSet, self).create(request, *args, ** kwargs)

    def retrieve(self, request, pk=None, *args, **kwargs):
        return super(UserViewSet, self).retrieve(request, pk, *args, ** kwargs)

    def partial_update(self, request, pk=None, *args, **kwargs):
        return super(UserViewSet, self).partial_update(request, pk, *args, ** kwargs)

    def destroy(self, request, pk=None, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.is_active = False
            instance.save()
        except Http404:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_queryset(self):
        queryset = User.objects.filter(is_active=True)
        return queryset
