from django.urls import path
# import from app itself
from . import views 


urlpatterns = [
    path('<int:pk>/',views.detail,name="item_detail"),
    path('new/',views.new,name="new")
]
