from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    is_demarcheur = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.username}"
        # return f"{self.username} ({'Démarcheur' if self.is_demarcheur else 'Client'})"