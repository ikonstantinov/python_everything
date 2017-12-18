from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    birthday = models.DateField()
    about = models.CharField(max_length=2000)
