from django.db import models
from django.utils import timezone


class DomainNameServer(models.Model):
    address = models.CharField(max_length=40, blank=True) #адрес ДНС сервера


class Client(models.Model):

    login = models.CharField(max_length=30, null=False)
    password = models.CharField(max_length=30, null=False, blank=True)
    dns_server = models.CharField(max_length=30, null=False, blank=True) # доступные ДНС серверы


class Website(models.Model):
    name = models.CharField(max_length=50, null=False, blank=True) # адрес сайта
    address = models.CharField(max_length=40, null=False, blank=True) # IP-адрес сайта
    owner = models.CharField(max_length=40, null=False, blank=True) # связь с владельцем
    expires = models.DateTimeField(default=timezone.now() + timezone.timedelta(days=30)) # дата и время окончания аренды

