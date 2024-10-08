from django.shortcuts import redirect
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from .forms import RegisterForm, UserEditForm
from django.contrib import messages
from django.utils.translation import gettext as _
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import AccessMixin
import logging

log = logging.getLogger(__name__)


class AuthorRequiredMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if self.get_object().id != request.user.id:
            text_message = _("You don't have the rights to change another user")
            messages.error(request, text_message)
            return redirect('users')
        return super().dispatch(request, *args, **kwargs)


class UserUpdateView(AuthorRequiredMixin, SuccessMessageMixin, UpdateView):
    model = User
    template_name = 'users/update.html'
    form_class = UserEditForm
    success_message = _("The user has been successfully changed")
    success_url = reverse_lazy('users')


class UserDeleteView(AuthorRequiredMixin, SuccessMessageMixin, DeleteView):
    model = User
    template_name = 'users/delete.html'
    success_url = reverse_lazy('users')
    success_message = _("The user has been successfully deleted")


class UsersListView(ListView):
    model = User
    template_name = 'users/users_list.html'


class RegistrationView(SuccessMessageMixin, CreateView):
    form_class = RegisterForm
    template_name = 'users/registration.html'
    success_url = reverse_lazy('login')
    success_message = _("The user has been successfully registered")
