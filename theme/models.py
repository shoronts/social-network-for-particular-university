from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class usersIdeas(models.Model):
    date = models.DateTimeField(default=timezone.now)
    user = models.CharField(max_length=100, blank=False, null=False)
    first_name = models.CharField(max_length=100, blank=False, null=False)
    last_name = models.CharField(max_length=100, blank=False, null=False)
    comment = models.TextField(max_length=1000, blank=False, null=False)

    def __str__(self):
        return self.user
