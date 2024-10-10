from django.http import HttpResponse
from django.views import View
from django.views.generic.list import ListView
from task_manager.statuses.models import Statuses
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.contrib import messages


class LoginRequiredMsgMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            text_message = _("You are not logged in! Please log in")
            messages.error(request, text_message)
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class StatusesListView(LoginRequiredMsgMixin, ListView):
    login_url = reverse_lazy('login')
    model = Statuses
    template_name = 'statuses/statuses.html'


class StatusCreateView(LoginRequiredMsgMixin, View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Status create')


class StatusUpdateView(LoginRequiredMsgMixin, View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Status update')


class StatusDeleteView(LoginRequiredMsgMixin, View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Status delete')
