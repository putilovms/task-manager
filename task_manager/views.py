from django.views import View
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.utils import translation
from django.contrib import messages
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.utils.translation import gettext as _
import logging

log = logging.getLogger(__name__)


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
        log.debug(f'Язык переключён на - {lang}')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def login_message(sender, user, request, **kwargs):
    text_message = _("You have successfully logged in to the site")
    messages.success(request, text_message, fail_silently=True)


def logout_message(sender, user, request, **kwargs):
    text_message = _("You have successfully logged out of your account")
    messages.info(request, text_message, fail_silently=True)


# def page404(request, exception):
#     return render(request, '/404.html', status=404)


# def page500(request, exception):
#     return render(request, '/500.html', status=500)


user_logged_in.connect(login_message)
user_logged_out.connect(logout_message)
