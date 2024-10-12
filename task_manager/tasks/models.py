from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from task_manager.statuses.models import Statuses
from task_manager.labels.models import Labels


class Tasks(models.Model):
    name = models.CharField(
        max_length=30,
        unique=True,
        verbose_name=_('Name'),
    )
    description = models.CharField(
        max_length=255,
        blank=True,
        verbose_name=_('Description'),
    )
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='author',
        verbose_name=_('Author'),
    )
    executor = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='executor',
        null=True,
        blank=True,
        verbose_name=_('Executor'),
    )
    status = models.ForeignKey(
        Statuses,
        on_delete=models.PROTECT,
        verbose_name=_('Status'),
    )
    labels = models.ManyToManyField(
        Labels,
        through="LabelsTasks",
        verbose_name=_('Labels'),
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Task')


class LabelsTasks(models.Model):
    task = models.ForeignKey(Tasks, on_delete=models.CASCADE)
    label = models.ForeignKey(Labels, on_delete=models.PROTECT)
