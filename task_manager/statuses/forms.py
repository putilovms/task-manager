from django.forms import ModelForm
from task_manager.statuses.models import Statuses


class StatusesForm(ModelForm):
    class Meta:
        model = Statuses
        fields = ['name']
