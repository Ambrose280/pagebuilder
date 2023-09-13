
from django.contrib import admin
from django.urls import path
from django_grapesjs.views.get_template import GetTemplate

urlpatterns = [
    path("admin/", admin.site.urls),
    path('get_template/', GetTemplate.as_view(), name='dgjs_get_template'),
]
