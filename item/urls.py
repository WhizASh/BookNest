from django.urls import path
# import from app itself
from . import views 


urlpatterns = [
    path('',views.browse,name="browse"),
    path('<int:pk>/',views.detail,name="item_detail"),
    path('<int:pk>/delete',views.delete_item,name="delete_item"),
    path('<int:pk>/edit',views.edit,name="edit"),
    
    path('new/',views.new,name="new")
]
