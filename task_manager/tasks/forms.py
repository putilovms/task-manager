from task_manager.tasks.models import Tasks
from django.forms import ModelForm, Textarea


class TasksForm(ModelForm):
    class Meta:
        model = Tasks
        fields = ['name', 'description', 'status', 'executor']
        widgets = {
            'description': Textarea(),
        }
