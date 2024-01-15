from django.urls import path
#django predefined login form import 
from django.contrib.auth import views as auth_views
from .forms import Loginform
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('contact/',views.contact,name="contact"),
    path('signup/',views.signup,name="form"),
    path('logout/',views.logout,name="logout"),
    #try to make the own login form since i don't fully know this prebuild django login form
    path('login/',auth_views.LoginView.as_view(template_name="core/login.html",authentication_form = Loginform),name="login"),

    #actual paths
    path('browse/',views.browse,name="browse"),
    path('home/',views.home,name="home"),
]
