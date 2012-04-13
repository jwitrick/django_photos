from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    url(r'(?P<username>\w{0,50})/(?P<category>\w{0,30})/(?P<gallery>\w{0,50})/$', 'photos.views.cust_cat_gallery_detail', name='customer_cat_gallery_detail'),
    url(r'(?P<username>\w{0,50})/(?P<category>\w{0,30})/$', 'photos.views.cust_cat_detail', name='customer_cat_detail'),
    url(r'(?P<username>\w{0,50})/$', 'photos.views.cust_detail', name='customer_detail'),
    url(r'^$', 'photos.views.index'),
)

#url(r'^login/$', "django.contrib.auth.views.login", {'template_name': 'photos/auth.html'}),
# url(r'^django_photos/', include('django_photos.foo.urls')),
# Uncomment the admin/doc line below to enable admin documentation:
# url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

# Uncomment the next line to enable the admin:
