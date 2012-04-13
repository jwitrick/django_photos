from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):

    class Meta:
        db_table = 'categories'
        verbose_name_plural = 'categories'
        app_label = 'photos'

    name = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(blank=True)

    def __unicode__(self):
        return u"%s"%self.name

    def user_name(self):
        return self.user
