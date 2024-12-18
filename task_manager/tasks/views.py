from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django_filters.views import FilterView
from task_manager.mixins import AuthorRequiredMixin, LoginRequiredMsgMixin
from task_manager.tasks.models import Tasks

from .filters import MyFilter
from .forms import TasksForm


class TasksListView(LoginRequiredMsgMixin, FilterView):
    login_url = reverse_lazy('login')
    model = Tasks
    template_name = 'tasks/tasks_list.html'
    filterset_class = MyFilter


class TasksCreateView(LoginRequiredMsgMixin, SuccessMessageMixin, CreateView):
    login_url = reverse_lazy('login')
    form_class = TasksForm
    template_name = 'tasks/task_create.html'
    success_url = reverse_lazy('tasks')
    success_message = _("The task has been successfully created")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TasksDeleteView(
    LoginRequiredMsgMixin,
    AuthorRequiredMixin,
    SuccessMessageMixin,
    DeleteView
):
    login_url = reverse_lazy('login')
    context_object_name = 'task'
    model = Tasks
    template_name = 'tasks/task_delete.html'
    success_url = reverse_lazy('tasks')
    success_message = _("The task was successfully deleted")


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
