from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from task_manager.statuses.models import Statuses


class Tasks(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING,
                               related_name='author')
    executor = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, related_name='executor', null=True)
    status = models.ForeignKey(Statuses, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Task')
