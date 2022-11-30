from django.db import models
from django_fsm import FSMField, transition


class Hit(models.Model):
    created_by = models.ForeignKey('users.User', related_name='creator', on_delete=models.CASCADE)
    assigned_to = models.ForeignKey('users.User', related_name='assigned', on_delete=models.CASCADE,null=True)
    description = models.CharField(max_length=100)
    objetive_name = models.CharField(max_length=100)
    state = FSMField(default='Assigned')
    created_on = models.DateTimeField(auto_now_add=True, blank=True)

    @transition(field=state, source="Assigned", target="Failed")
    def failed(self):
        pass

    @transition(field=state, source="Assigned", target="Completed")
    def completed(self):
        pass

    class Meta:
        ordering = ['-created_on']
