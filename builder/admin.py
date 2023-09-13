from django.contrib import admin
from django_grapesjs.admin import GrapesJsAdminMixin
from .models import *

@admin.register(BuildHTML)
class ExampleAdmin(GrapesJsAdminMixin, admin.ModelAdmin):
    pass