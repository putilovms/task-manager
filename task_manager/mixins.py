from django.contrib import messages
from django.http import HttpResponseRedirect
from django.db.models import ProtectedError
from django.contrib.auth.mixins import AccessMixin
from django.utils.translation import gettext_lazy as _
from django.shortcuts import redirect


class ProtectedMessageMixin:
    protected_error_message = ''

    def post(self, request, *args, **kwargs):
        self.request = request
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        success_url = self.get_success_url()
        try:
            super().form_valid(form)
        except ProtectedError:
            messages.error(self.request, self.protected_error_message)
        return HttpResponseRedirect(success_url)


class LoginRequiredMsgMixin(AccessMixin):
    not_logged_message = _("You are not logged in! Please log in")
    redirect_field_name = None

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, self.not_logged_message)
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class AuthorRequiredMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if self.get_object().author.id != request.user.id:
            text_message = _("Only the author of the task can delete it")
            messages.error(request, text_message)
            return redirect('tasks')
        return super().dispatch(request, *args, **kwargs)
