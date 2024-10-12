import django_filters
from task_manager.tasks.models import Tasks
from task_manager.labels.models import Labels


class MyFilter(django_filters.FilterSet):
    labels = django_filters.ModelChoiceFilter(
        field_name='labels',
        queryset=Labels.objects.all(),
    )

    class Meta:
        model = Tasks
        fields = ['status', 'executor', 'labels']
