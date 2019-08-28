from django.urls import include, path
from rest_framework import routers

from core import views

router = routers.DefaultRouter()

router.register(
    r'sites',
    views.SiteViewSet,
    base_name='sites')

router.register(
    r'site-users',
    views.SiteUserViewSet,
    base_name='site-users')

router.register(
    r'users',
    views.UserViewSet,
    base_name='users')

urlpatterns = [
    path('api/', include(router.urls)),

]
