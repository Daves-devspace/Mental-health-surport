
from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('grappelli/', include('grappelli.urls')), # grappelli URLS
    
    path('admin/', admin.site.urls),
    
    path('',include('home.urls')),
    
    path('packages/',include('home.urls'))
   
]

