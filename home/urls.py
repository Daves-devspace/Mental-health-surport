from django.urls import path

from . import views

urlpatterns = [
    path('resources',views.resources,name='resources'),
    path('my-login',views.my_login,name='my_login'),
    path('register',views.register,name='register'),
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('packages-filter',views.packages,name='packages-filter')
]