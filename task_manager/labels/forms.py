from django.forms import ModelForm
from task_manager.labels.models import Labels


class LabelsForm(ModelForm):
    class Meta:
        model = Labels
        fields = ['name']
