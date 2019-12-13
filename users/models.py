from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

JAMB_SCORES = [
  "English",
  "Maths",
  "Physics",
  "Chemistry",
  "Biology",
]

subjects = {
  "Medicine": [0,2,3,4],
  "Engineering": [0,1,3,4],
  "Law": [0,]
}

class User(AbstractUser):
  """Model definition for User."""

  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)


  class Meta:
    """Meta definition for MODELNAME."""
    verbose_name = 'User'
    verbose_name_plural = 'Users'

  def __str__(self):
    """Unicode representation of MODELNAME."""
    return self.username


class Suggest(models.Model):
  """Model definition for Suggest."""


  class Meta:
    """Meta definition for Suggest."""

    verbose_name = 'Suggest'
    verbose_name_plural = 'Suggests'

  def __str__(self):
    """Unicode representation of Suggest."""
    pass
