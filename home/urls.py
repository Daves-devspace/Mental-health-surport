from django.urls import path

from . import views

urlpatterns = [
    path('resources',views.resources),
    path('my-login',views.my_login),
    path('register',views.register),
    path('',views.home)
]