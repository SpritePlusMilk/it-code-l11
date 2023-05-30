from django import forms
from core import models

forbidden_characters = "'!@#$%^&*()\/"


class ClientForm(forms.ModelForm):
    login = forms.CharField(label='логин клиента',required=True)
    password = forms.CharField(label='пароль клиента', required=True)

    class Meta:
        model = models.Client
        fields = '__all__'


class ClientSearch(forms.Form):

    def clean_client_login(self):
        login = list(self.cleaned_data['client_login'])
        if list(filter(lambda x: x in forbidden_characters, login)):
            raise forms.ValidationError(f'Имя не должно содержать символов {forbidden_characters}')
        return login
    client_login = forms.CharField(label='Логин клиента',required=False)


class WebsiteSearch(forms.Form):
    website_name = forms.CharField(label='поиск по имени сайта', required=False)
    website_url = forms.CharField(label='поиск по адресу сайта', required=False)
    website_owner = forms.CharField(label='поиск по владельцу сайта', required=False)

    def clean(self):
        name = list(self.cleaned_data['website_name'])
        url = list(self.cleaned_data['website_url'])
        owner = list(self.cleaned_data['website_owner'])
        if list(filter(lambda x: x in forbidden_characters, name)):
            raise forms.ValidationError(f'Имя сайта не должно содержать символов {forbidden_characters}')

        if list(filter(lambda x: x in forbidden_characters, url)):
            raise forms.ValidationError(f'Адрес не должен содержать символов {forbidden_characters}')

        if list(filter(lambda x: x in forbidden_characters, owner)):
            raise forms.ValidationError(f'Имя влдельца не должно содержать символов {forbidden_characters}')
        return name
