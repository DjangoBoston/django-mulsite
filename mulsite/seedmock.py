from django.contrib.auth import get_user_model
from django.contrib.sites.models import Site

from core.models import SiteUser

mock_domains = ['alpha.devsite', 'bravo.devsite', 'charlie.devsite']

mock_data = {
    'alpha.devsite': ['useralpha1', 'useralpha2'],
    'bravo.devsite': ['userbravo1', 'userbravo2'],
    'charlie.devsite': ['usercharlie1', 'usercharlie2'],
}


def seed_all():
    for domain, usernames in mock_data.items():
        site = Site.objects.create(domain=domain, name=domain)
        for username in usernames:
            user = get_user_model().objects.create_user(
                    username=username,
                    email='{0}@{1}'.format(username, domain),
                    password='nopass',
                )
            SiteUser.objects.create(site=site, user=user)


def wipe():
    Site.objects.exclude(domain='example.com').delete()
    get_user_model().objects.exclude(is_superuser=True).delete()
    SiteUser.objects.all().delete()
