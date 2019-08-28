from django.contrib import admin

# Register your models here.

from core.models import SiteUser


@admin.register(SiteUser)
class SiteUserAdmin(admin.ModelAdmin):
    pass
