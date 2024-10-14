from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from .forms import RegisterForm, UserEditForm
from django.utils.translation import gettext as _
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from task_manager.mixins import ProtectedMessageMixin, UserCreatorRequiredMixin

User.__str__ = lambda user_instance: user_instance.get_full_name()


class UserUpdateView(UserCreatorRequiredMixin, SuccessMessageMixin, UpdateView):
    model = User
    template_name = 'users/user_update.html'
    form_class = UserEditForm
    success_message = _("The user has been successfully changed")
    success_url = reverse_lazy('users')


class UserDeleteView(
    UserCreatorRequiredMixin,
    ProtectedMessageMixin,
    SuccessMessageMixin,
    DeleteView
):
    model = User
    template_name = 'users/user_delete.html'
    success_url = reverse_lazy('users')
    success_message = _("The user has been successfully deleted")
    protected_error_message = _(
        "It is not possible to delete a user because it is being used")


class UsersListView(ListView):
    model = User
    template_name = 'users/users.html'


class RegistrationView(SuccessMessageMixin, CreateView):
    form_class = RegisterForm
    template_name = 'users/user_create.html'
    success_url = reverse_lazy('login')
    success_message = _("The user has been successfully registered")
