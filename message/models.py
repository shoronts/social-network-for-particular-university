from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class allmessage(models.Model):

    current_date = models.DateTimeField(default=timezone.now)
    user = models.CharField(max_length=100, blank=False, null=False)
    user1 = models.CharField(max_length=100, blank=False, null=False)
    message = models.CharField(max_length=1000, blank=True, null=True)
    message1 = models.CharField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.user
        