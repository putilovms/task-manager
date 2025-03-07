from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from task_manager.mixins import LoginRequiredMsgMixin, ProtectedMessageMixin
from task_manager.statuses.models import Statuses

from .forms import StatusesForm


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


class StatusUpdateView(LoginRequiredMsgMixin, SuccessMessageMixin, UpdateView):
    login_url = reverse_lazy('login')
    context_object_name = 'status'
    model = Statuses
    form_class = StatusesForm
    template_name = 'statuses/status_update.html'
    success_url = reverse_lazy('statuses')
    success_message = _("The status has been successfully changed")


class StatusDeleteView(
    LoginRequiredMsgMixin,
    ProtectedMessageMixin,
    SuccessMessageMixin,
    DeleteView
):
    login_url = reverse_lazy('login')
    context_object_name = 'status'
    model = Statuses
    template_name = 'statuses/status_delete.html'
    success_url = reverse_lazy('statuses')
    success_message = _("The status has been successfully deleted")
    protected_error_message = _(
        "It is not possible to delete the status because it is in use")
