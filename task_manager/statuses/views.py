from django.http import HttpResponse
from django.views.generic.list import ListView
from task_manager.statuses.models import Statuses
from django.contrib.auth.mixins import AccessMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.contrib import messages
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from .forms import StatusesForm


class LoginRequiredMsgMixin(AccessMixin):
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


class StatusCreateView(LoginRequiredMsgMixin, SuccessMessageMixin, CreateView):
    login_url = reverse_lazy('login')
    form_class = StatusesForm
    template_name = 'statuses/status_create.html'
    success_url = reverse_lazy('statuses')
    success_message = _("The status has been successfully created")


class StatusUpdateView(LoginRequiredMsgMixin, UpdateView):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Status update')


class StatusDeleteView(LoginRequiredMsgMixin, DeleteView):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Status delete')
