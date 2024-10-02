from django.views import View
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.utils import translation


class HomePageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html', context={})


class SetLang(View):
    langs = {
        'en': 'en-us',
        'ru': 'ru-RU',
    }

    def get(self, request, *args, **kwargs):
        lang = self.langs.get(kwargs['lang'], self.langs['ru'])
        translation.activate(lang)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
