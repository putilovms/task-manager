from django.db import models
from django.utils.translation import gettext_lazy as _

class Statuses(models.Model):
    name = models.CharField(max_length=30, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _('Task status')
