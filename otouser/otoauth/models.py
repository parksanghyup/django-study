from django.db import models
from django.contrib.auth.models import User

class ExtraUserData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    something = models.TextField(blank=True)
