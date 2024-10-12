# from django.views.generic.list import ListView
# from task_manager.statuses.models import Statuses
from django.contrib.auth.mixins import AccessMixin
# from django.contrib.messages.views import SuccessMessageMixin
# from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.contrib import messages
# from django.views.generic.edit import DeleteView, CreateView, UpdateView
# from .forms import StatusesForm


class LoginRequiredMsgMixin(AccessMixin):
    redirect_field_name = None

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            text_message = _("You are not logged in! Please log in")
            messages.error(request, text_message)
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


# class LabelsListView(LoginRequiredMsgMixin, ListView):
#     login_url = reverse_lazy('login')
#     model = Statuses
#     template_name = 'labels/labels.html'


# class LabelCreateView(LoginRequiredMsgMixin, SuccessMessageMixin, CreateView):
#     login_url = reverse_lazy('login')
#     form_class = StatusesForm
#     template_name = 'labels/label_create.html'
#     success_url = reverse_lazy('statuses')
#     success_message = _("The status has been successfully created")


# class LabelUpdateView(LoginRequiredMsgMixin, SuccessMessageMixin, UpdateView):
#     login_url = reverse_lazy('login')
#     context_object_name = 'label'
#     model = Statuses
#     form_class = StatusesForm
#     template_name = 'labels/label_update.html'
#     success_url = reverse_lazy('statuses')
#     success_message = _("The status has been successfully changed")


# class LabelDeleteView(LoginRequiredMsgMixin, SuccessMessageMixin, DeleteView):
#     login_url = reverse_lazy('login')
#     context_object_name = 'label'
#     model = Statuses
#     template_name = 'labels/label_delete.html'
#     success_url = reverse_lazy('statuses')
#     success_message = _("The status has been successfully deleted")
