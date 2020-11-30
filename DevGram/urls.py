

from os import name
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from DevGram import view
from posts import views as post_views
from users import views as users_views

urlpatterns = [

    path('admin/', admin.site.urls, name='django'),

    path('hello/', view.hello_world, name='hello_world'),
    path('test/',view.sort_integers, name='sorted'),
    path('social/<str:name>/<int:age>/',view.age_user, name='hi'),

    path('',post_views.list_posts, name='feed'),
    path('posts/new/',post_views.create_post, name='create_post'),

    path('users/login/',users_views.login_view,name='login'),
    path('users/logout/',users_views.logout_view,name='logout'),
    path('users/signup/',users_views.signup,name='signup'),
    path('users/me/profile/',users_views.update_profile,name='update_profile'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
