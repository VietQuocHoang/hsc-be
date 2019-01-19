from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import UserManager
UserModel = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        return UserModel.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            password = validated_data.pop('password')
            password = make_password(password)
            validated_data['password'] = password
        return super(UserSerializer, self).update(instance, validated_data)

    class Meta:
        model = UserModel
        fields = (
            'pk', 'username', 'password', 'email',
            'is_superuser', 'is_staff', 'first_name', 'last_name'
        )
