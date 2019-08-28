from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.sites.models import Site


class SiteUser(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
