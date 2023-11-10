"""Models of the API """

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Contact(models.Model):
    """User contact model"""

    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField()
    local_phone = models.CharField(max_length=30)
    mobile_phone = models.CharField(max_length=30)
    user = models.ForeignKey(to=User, on_delete=models.PROTECT, name="contacts")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
