"""Serializers"""

from rest_framework import serializers
from django.contrib.auth.models import User
from api import models


class UserModelSerializer(serializers.ModelSerializer):
    """
    Users from Django used as authentication
    """

    class Meta:
        model = User
        fields = (
            "username",
            "password",
            "email",
        )

    def create(self, validated_data):
        return self.Meta.model.objects.create_user(**validated_data)


class ContactModelSerializer(serializers.ModelSerializer):
    """
    Contacts for Users serializer
    """

    class Meta:
        model = models.Contact
        fields = (
            "id",
            "user",
            "first_name",
            "last_name",
            "email",
            "local_phone",
            "mobile_phone",
        )
