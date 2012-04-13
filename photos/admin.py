from photos.models.gallery import Gallery
from photos.models.category import Category
from photos.models.userprofile import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from django.db.models.signals import pre_delete, post_save

admin.site.unregister(User)

class UserProfileInline(admin.StackedInline):
    model = UserProfile

class UserProfileAdmin(UserAdmin):
    inlines = [UserProfileInline]

    def save_model(self, request, obj, form, change):
        obj.save()
        if not change:
            cat_name = 'default'
            desc = 'This is the default category all galleries go into'
            c = Category(name=cat_name, user=obj, description=desc)
            c.save()

admin.site.register(User, UserProfileAdmin)

class GalleryAdmin(admin.ModelAdmin):
    list_display = ('name', 'user_name', "public")

    def save_model(self, request, obj, form, change):
        if not change:
            assert obj._create_new_gallery()

        """
        if change == true then its modifying an existing gallery. I will need to
        do some checks to determine if hte gallery has moved from one user to
        another.
        """
        obj.save()

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'user_name')

admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Category, CategoryAdmin)

def _delete(sender, **kwargs):
    obj = kwargs['instance']
    obj._delete()

pre_delete.connect(_delete, sender=Gallery)

