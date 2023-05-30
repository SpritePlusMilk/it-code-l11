import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hosting.settings')
django.setup()

from django.test import TestCase, Client
from django.urls import reverse
from core import models


class WebsiteTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.clien = models.Client.objects.create(login='usr6', password='123123', dns_server='dns.dns.6')
        self.website = models.Website.objects.create(
            name='wsite3', address='www.w3.com',
            owner='ownerr',expires='2023-01-01 11:11')

    def test_client_list(self):
        response = self.client.get(reverse('core:cl_list'))
        self.assertEqual(response.status_code, 200)

    def test_website_list(self):
        response = self.client.get(reverse('core:ws_list'))
        self.assertEqual(response.status_code, 200)

    def test_detail_website(self):
        response = self.client.get(reverse('core:detail_ws', kwargs={'pk' : self.website.pk}))
        self.assertEqual(response.status_code, 200)

    def test_detail_client(self):
        response = self.client.get(reverse('core:detail_cl', kwargs={'pk' : self.clien.pk}))
        self.assertEqual(response.status_code, 200)

    def test_create_client(self):
        context = {
            'login': 'user11',
            'password': 'password123123',
            'dns_server':'dnsdns'
        }
        response = self.client.post(path=reverse('core:cl_create'), data=context, follow=True)
        self.assertEqual(response.status_code, 200)
