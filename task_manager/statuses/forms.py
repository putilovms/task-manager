from task_manager.statuses.models import Statuses
from django.forms import ModelForm
from django.utils.translation import gettext as _


class StatusesForm(ModelForm):
    class Meta:
        model = Statuses
        fields = ['name']
        labels = {
            'name': _('Name'),
        }
