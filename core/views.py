
from django.contrib.sites.models import Site
from django.contrib.auth import get_user_model
from django.contrib.sites.shortcuts import get_current_site

from rest_framework import viewsets

from core.models import SiteUser
from core import sites
from core.serializers import SiteUserSerializer, SiteSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    model = get_user_model()
    serializer_class = UserSerializer

    def get_queryset(self):
        site = get_current_site(self.request)
        queryset = sites.get_users_for_site(site)
        return queryset


class SiteUserViewSet(viewsets.ModelViewSet):
    model = SiteUser
    serializer_class = SiteUserSerializer

    def get_queryset(self):
        site = get_current_site(self.request)
        queryset = sites.get_siteusers_for_site(site)
        return queryset


class SiteViewSet(viewsets.ReadOnlyModelViewSet):
    """
    TODO: Restrict this viewset to global admins
    Example: Users who have `is_superuser` set to `True`
    """
    model = Site
    queryset = Site.objects.all()
    serializer_class = SiteSerializer
