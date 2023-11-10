"""
Views for an API
"""

from rest_framework import viewsets, response, decorators, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth.models import User
from api import models, serializers as api_serializers


class UserViewSet(viewsets.ViewSet):
    """User signs in"""

    serializer_class = api_serializers.UserModelSerializer
    authentication_classes = []
    permission_classes = []

    def create(self, request):
        the_serializer = self.serializer_class(data=request.data)

        the_serializer.is_valid(raise_exception=True)

        user = the_serializer.save()

        return response.Response(
            {"message": f"User {user.username} was created successfully"}
        )


class ContactViewSet(viewsets.ModelViewSet):
    serializer_class = api_serializers.ContactModelSerializer

    queryset = models.Contact.objects.all()

    def get_queryset(self):
        return models.Contact.objects.filter(user=self.request.user)
