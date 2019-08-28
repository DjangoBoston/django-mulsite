
from django.contrib.auth import get_user_model
from django.contrib.sites.models import Site
from rest_framework import serializers

from core.models import SiteUser


class SiteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Site
        exclude = ()


class SiteUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteUser
        exclude = ()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        exclude = ('password',)
