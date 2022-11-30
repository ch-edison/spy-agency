from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.db import models
from apps.system_hits.models import Hit
from django_fsm import FSMField, transition


class User(AbstractUser):
    name = models.CharField(_('Name'), blank=True, max_length=20)
    description = models.CharField(_('Description'), blank=True, max_length=20)
    hits = models.ManyToManyField(Hit)
    manager = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    state = FSMField(default='Active')

    @transition(field=state, source="Active", target="Inactive")
    def inactive(self):
        pass