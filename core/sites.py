
from django.contrib.auth import get_user_model
from core.models import SiteUser


def get_siteusers_for_site(site):
    return SiteUser.objects.filter(site=site)


def get_user_ids_for_site(site):
    mappings = SiteUser.objects.filter(site=site)
    return mappings.values_list('user_id')


def get_users_for_site(site):
    user_ids = get_user_ids_for_site(site)
    return get_user_model().objects.filter(id__in=user_ids)
