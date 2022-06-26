from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseModelStatus(models.IntegerChoices):
    ACTIVE = 1, _('Active')
    SUSPENDED = 0, _('Suspended')
    DELETED = -1, _('Deleted')
