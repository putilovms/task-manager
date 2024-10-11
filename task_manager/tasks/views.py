from django.http import HttpResponse
from django.views import View
from django.contrib.auth.mixins import AccessMixin
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from task_manager.tasks.models import Tasks
from .forms import TasksForm
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
# , DeleteView


class LoginRequiredMsgMixin(AccessMixin):
    redirect_field_name = None

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            text_message = _("You are not logged in! Please log in")
            messages.error(request, text_message)
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class TasksListView(LoginRequiredMsgMixin, ListView):
    login_url = reverse_lazy('login')
    model = Tasks
    template_name = 'tasks/tasks_list.html'


class TasksCreateView(LoginRequiredMsgMixin, SuccessMessageMixin, CreateView):
    login_url = reverse_lazy('login')
    form_class = TasksForm
    template_name = 'tasks/task_create.html'
    success_url = reverse_lazy('tasks')
    success_message = _("The task has been successfully created")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TasksDeleteView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Task delete')


class TasksUpdateView(LoginRequiredMsgMixin, SuccessMessageMixin, UpdateView):
    login_url = reverse_lazy('login')
    context_object_name = 'task'
    model = Tasks
    form_class = TasksForm
    template_name = 'tasks/task_update.html'
    success_url = reverse_lazy('tasks')
    success_message = _("The task has been successfully changed")


class TaskView(LoginRequiredMsgMixin, DetailView):
    login_url = reverse_lazy('login')
    model = Tasks
    template_name = 'tasks/task.html'
    context_object_name = 'task'
