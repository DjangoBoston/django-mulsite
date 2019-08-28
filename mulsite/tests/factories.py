
from django.contrib.auth import get_user_model
from django.contrib.sites.models import Site

import factory

from core.models import SiteUser


class UserFactory(factory.DjangoModelFactory):
    class Meta:
        model = get_user_model()

    username = factory.Sequence(lambda n: 'user{}'.format(n))
    password = factory.PostGenerationMethodCall('set_password', 'password')
    email = factory.LazyAttribute(lambda a: '{0}@example.com'.format(a.username))
    is_active = True
    is_staff = False
    is_superuser = False


class SiteFactory(factory.DjangoModelFactory):
    class Meta:
        model = Site
    domain = factory.Sequence(lambda n: 'site-{}.example.com'.format(n))
    name = factory.Sequence(lambda n: 'Site {}'.format(n))


class SiteUserFactory(factory.DjangoModelFactory):
    class Meta:
        model = SiteUser
    site = factory.SubFactory(SiteFactory)
    user = factory.SubFactory(UserFactory)
