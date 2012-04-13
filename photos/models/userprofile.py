
from datetime import datetime
from django.db import models
from django.contrib.auth.models import User, UserManager

class UserProfile(models.Model):
    class Meta:
        app_label = 'photos'
        db_table = 'userprofile'

    user= models.OneToOneField(User)
    description = models.TextField(blank=True)


User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
