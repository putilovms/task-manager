from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from task_manager.statuses.models import Statuses


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
        on_delete=models.DO_NOTHING,
        related_name='author',
        verbose_name=_('Author'),
    )
    executor = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        related_name='executor',
        null=True,
        blank=True,
        verbose_name=_('Executor'),
    )
    status = models.ForeignKey(
        Statuses,
        on_delete=models.DO_NOTHING,
        verbose_name=_('Status'),
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Task')
