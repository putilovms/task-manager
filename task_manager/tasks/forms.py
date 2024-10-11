from task_manager.tasks.models import Tasks
from django.forms import ModelForm, Textarea
from django.utils.translation import gettext_lazy as _


class TasksForm(ModelForm):
    class Meta:
        model = Tasks
        fields = ['name', 'description', 'status', 'executor']
        labels = {
            'name': _('Name'),
            'description': _('Description'),
            'status': _('Status'),
            'executor': _('Executor'),
        }
        widgets = {
            'description': Textarea(),
        }
