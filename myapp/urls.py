from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.login,name='login'),
    path('home/', views.home, name='home'),
    path('admin_home/', views.admin_home, name='admin_home'),
    path('signup/', views.signup,name='signup'),
    path('register_user/', views.register_user, name='register_user'),
    path('logout/', views.logout, name='logout'),
    path('create_post/', views.createPost, name='create_post'),

    path('readmore/<int:id>', views.readmore, name='readmore'),

]
