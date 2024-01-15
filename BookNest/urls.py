from django.contrib import admin
from django.urls import path, include
from core.views import index , contact

#for image to server
from django.conf import settings
from django.conf.urls.static import static

#to change the text of the admin panel
admin.site.site_header = "BookNest Admin"
admin.site.site_title = "BookNest Admin Portal"
admin.site.index_title = "Edit the listings on BookNest"


urlpatterns = [
    path('admin/', admin.site.urls),
    #app specific url path are included and routed to the app url.py file

    #core has basic page home , browse page , sign up 
    path('',include('core.urls')), 
    #item has item detail page and item search  logic 
    path('item/',include('item.urls')),
    #dashboard has logged in users info 
    path('dashboard/',include('dashboard.urls')),

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)    #added this path to allow django to serve images via media url
