from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from core import models, forms


class TitleMixin:
    title = None

    def get_title(self):
        return self.title

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.get_title()
        return context


def index(request):
    return render(request=request, template_name='core/index.html')


class ClientsList(ListView, TitleMixin):
    model = models.Client
    template_name = 'core/clients_list.html'
    context_object_name = 'clients'

    def get_queryset(self):
        client_login = self.request.GET.get('client_login')
        qset = models.Client.objects.all()
        if client_login:
            return qset.filter(login__icontains=client_login)
        return qset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = forms.ClientSearch(self.request.GET)
        return context


class DetailClient(DetailView):
    model = models.Client
    template_name = 'core/client.html'
    context_object_name = 'client'


class CreateClient(CreateView):
    model = models.Client
    template_name = 'core/create_client.html'
    form_class = forms.ClientForm
    success_url = reverse_lazy('core:cl_list')


class UpdateClient(UpdateView):
    model = models.Client
    template_name = 'core/client_update.html'
    form_class = forms.ClientForm
    success_url = reverse_lazy('core:cl_list')


class DeleteClient(DeleteView):
    model = models.Client
    template_name = 'core/client_delete.html'
    success_url = reverse_lazy('core:cl_list')


class WebsitesList(ListView, TitleMixin):
    model = models.Website
    template_name = 'core/websites_list.html'
    context_object_name = 'websites'

    def get_queryset(self):
        website_name = self.request.GET.get('website_name')
        website_url = self.request.GET.get('website_url')
        website_owner = self.request.GET.get('website_owner')
        qset = models.Website.objects.all()
        if website_name:
            return qset.filter(Q(name__icontains=website_name) | Q(address__icontains=website_url) | Q(owner=website_owner))
        return qset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = forms.WebsiteSearch(self.request.GET)
        return context


class DetailWebsite(DetailView):
    model = models.Website
    template_name = 'core/website.html'
    context_object_name = 'website'

