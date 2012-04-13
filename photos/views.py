# Create your views here.
from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response, get_object_or_404
from django.core.context_processors import csrf
from photos.models.customer import Customer
from photos.models.userprofile import UserProfile
from photos.models.gallery import Gallery
from photos.models.category import Category
from django.contrib.auth.models import User

def index(request):
    cust_users = _get_all_users_except_staff()
    return render_to_response('photos/index.html', {'users':cust_users})

def login(request):
    print "GETTING HERE"

def cust_detail(request, username):
    user = get_object_or_404(User, username=username)
    c = get_object_or_404(UserProfile, user=user)
    categories = []
    cus_categories = _get_all_categories_for_user(user)
    categories.extend(cus_categories)
    return render_to_response('photos/cust_detail.html', {'user': user, 'userprofile':c, 'categories': categories})

def cust_cat_detail(request, username, category):
    user = get_object_or_404(User, username=username)
    c = get_object_or_404(Category, name=category, user=user)
    galleries = _get_all_galleries_for_user_by_category(user, c)
    return render_to_response('photos/cust_cat_detail.html', {'user':user, 'category':category, 'galleries': galleries})

def cust_cat_gallery_detail(reques, username, category, gallery):
    user = get_object_or_404(User, username=username)
    gallery = get_object_or_404(Gallery, name=gallery, user=user)
    files = gallery._get_thumbnail_photos_in_gallery()
    return render_to_response('photos/cust_gallery_show.html', {'photos':files})
    #return render_to_response('photos/cust_gallery_show_galleriffic.html', {'photos':files})

def _get_all_users_except_staff():
    try:
        users = list(User.objects.filter(is_staff=False, is_active=True))
    except User.DoesNotExist:
        users = []
    return users

def _get_all_categories_for_user(user):
    try:
        categories = list(Category.objects.filter(user=user))
    except Category.DoesNotExist:
        categories = []
    return categories

def _get_all_galleries_for_user_by_category(user, category):
    try:
        galleries = list(Gallery.objects.filter(user=user, category=category))
    except Gallery.DoesNotExist:
        galleries = []
    return galleries
