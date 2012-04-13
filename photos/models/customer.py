
from django.db import models
from datetime import datetime
from django.shortcuts import get_object_or_404

# Create your models here.
class Customer(models.Model):
    class Meta:
        db_table = 'customers'
        app_label = 'photos'
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField('password', max_length=128)
    email = models.EmailField(unique=True)
    last_login_time = models.DateTimeField(default=datetime.now())
    enabled = models.BooleanField()
    description = models.TextField(blank=True)

    def __unicode__(self):
        return u"%s"%self.username

#    def __unicode__(self):
#        return u"'%s', '%s', '%s', '%s'"%(
#                self.username,
#                self.email,
#                self.last_login_time,
#                self.enabled)

