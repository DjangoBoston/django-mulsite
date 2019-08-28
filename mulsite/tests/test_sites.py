"""Tests 'core.sites' site isolation module

Inprovements
* Test creating a user with multiple accounts but same email address
"""
import pytest

from factories import SiteFactory, SiteUserFactory, UserFactory

from core.sites import get_users_for_site
from django.contrib.sites.models import Site


@pytest.mark.django_db
def test_create_siteuser():
    count_a = 3
    count_b = 4
    site_a = SiteFactory()
    site_b = SiteFactory()

    assert site_a.domain != site_b.domain

    expected_users_a = [SiteUserFactory(site=site_a,
                                        user=UserFactory()) for i in range(count_a)]
    expected_users_b = [SiteUserFactory(site=site_b,
                                        user=UserFactory()) for i in range(count_b)]

    found_a = get_users_for_site(site=Site.objects.get(domain=site_a.domain))
    found_b = get_users_for_site(site=Site.objects.get(domain=site_b.domain))

    # May be overkill, but first testing counts, then test ids
    assert found_a.count() == len(expected_users_a)
    assert found_b.count() == len(expected_users_b)

    assert set(found_a.values_list('id', flat=True)) == set([obj.id for obj in expected_users_a])
    assert set(found_b.values_list('id', flat=True)) == set([obj.id for obj in expected_users_b])
