from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from task_manager.labels.models import Labels
from task_manager.mixins import LoginRequiredMsgMixin, ProtectedMessageMixin

from .forms import LabelsForm


class LabelsListView(LoginRequiredMsgMixin, ListView):
    login_url = reverse_lazy('login')
    model = Labels
    template_name = 'labels/labels.html'


class LabelCreateView(LoginRequiredMsgMixin, SuccessMessageMixin, CreateView):
    login_url = reverse_lazy('login')
    form_class = LabelsForm
    template_name = 'labels/label_create.html'
    success_url = reverse_lazy('labels')
    success_message = _("The label was created successfully")


class LabelUpdateView(LoginRequiredMsgMixin, SuccessMessageMixin, UpdateView):
    login_url = reverse_lazy('login')
    context_object_name = 'label'
    model = Labels
    form_class = LabelsForm
    template_name = 'labels/label_update.html'
    success_url = reverse_lazy('labels')
    success_message = _("The label has been successfully changed")


class LabelDeleteView(
    LoginRequiredMsgMixin,
    ProtectedMessageMixin,
    SuccessMessageMixin,
    DeleteView
):
    login_url = reverse_lazy('login')
    context_object_name = 'label'
    model = Labels
    template_name = 'labels/label_delete.html'
    success_url = reverse_lazy('labels')
    success_message = _("The label was successfully deleted")
    protected_error_message = _(
        "It is not possible to delete the label because it is being used")
