import django_filters
from task_manager.tasks.models import Tasks
from task_manager.labels.models import Labels
from django.forms import CheckboxInput
from django.utils.translation import gettext_lazy as _
from django_currentuser.middleware import get_current_user


class MyFilter(django_filters.FilterSet):
    label = django_filters.ModelChoiceFilter(
        field_name='labels',
        queryset=Labels.objects.all(),
        label=_('Label'),
    )
    self_tasks = django_filters.BooleanFilter(
        field_name='author',
        widget=CheckboxInput,
        method='filter_author',
        label=_('Only your own tasks'),
    )

    def filter_author(self, queryset, name, value):
        if value:
            user = get_current_user()
            queryset = queryset.filter(author__exact=user.id)
        return queryset

    class Meta:
        model = Tasks
        fields = ['status', 'executor']
