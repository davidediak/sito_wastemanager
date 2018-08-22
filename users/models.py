from django.contrib.auth.models import AbstractUser, User
from django.db import models


# Create your models here.
class CustomUser(AbstractUser):
    # add additional fields in here
    #img = models.ImageField(null=True, upload_to="profile_url")
    country = models.CharField(null=True, max_length=50)
    city = models.CharField(null=True, max_length=50)
    #skills = models.ManyToManyField(Skill, through='HasSkill')

    def __str__(self):
        return self.username