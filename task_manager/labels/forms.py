from task_manager.labels.models import Labels
from django.forms import ModelForm


class LabelsForm(ModelForm):
    class Meta:
        model = Labels
        fields = ['name']
