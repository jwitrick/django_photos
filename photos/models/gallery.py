from django.db import models
from datetime import datetime
from category import Category
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from photos.utils.gallery_helper import GalleryHelper
from django.db.models.signals import pre_delete
from django.conf import settings

class Gallery(models.Model):
    class Meta:
        db_table = 'galleries'
        verbose_name_plural='galleries'
        app_label = 'photos'
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    public = models.BooleanField()
    password = models.CharField(max_length=128, null=True, blank=True)
    category = models.ForeignKey(Category)

    gh = GalleryHelper(settings.MEDIA_ROOT)

    def __unicode__(self):
        return "%s"%(self.name)

    def user_name(self, num=None):
        if not num:
            num = self.user.id
        c = get_object_or_404(User, pk=num)
        return c.username

    def _create_new_gallery(self):
        return self.gh._create_gallery(self.user.username, self.name)

    def _delete(self):
        return self._delete_gallery()

    def _delete_gallery(self):
        return self.gh._delete_gallery(self.user.username, self.name)

    def _get_photos_in_gallery(self):
        return self.gh._get_all_files_in_gallery(self.user.username, self.name)

    def _get_thumbnail_photos_in_gallery(self):
        return self.gh._get_all_thumbnail_files_in_gallery(self.user.username, self.name)
