from django.http import HttpResponse
from django.views import View
from django.contrib.auth.mixins import AccessMixin
from django.contrib import messages
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from task_manager.tasks.models import Tasks


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


class TasksCreateView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Task create')


class TasksDeleteView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Task delete')


class TasksUpdateView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Task update')


class TaskView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Task view')
