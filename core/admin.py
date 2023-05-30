from django.contrib import admin
from core import models


@admin.register(models.Client)
class Client(admin.ModelAdmin):
    list_display = ('login',)


@admin.register(models.Website)
class Website(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(models.DomainNameServer)
class DomainNameServer(admin.ModelAdmin):
    list_display = ('address',)
