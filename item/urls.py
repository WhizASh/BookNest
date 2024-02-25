from django.urls import path
# import from app itself
from . import views 


urlpatterns = [
    path('',views.old_browse,name="browse"),
    path('<int:pk>/',views.old_detail,name="item_detail"),
    path('browse/<int:pk>/delete',views.delete_item,name="delete_item"),
    path('browse/<int:pk>/edit',views.edit,name="edit"),
    
    path('new/',views.new,name="new"),

    #actual path
    path('browse/',views.browse,name="browse"),
    path('browse/<int:pk>/',views.detail,name="book_info"),
]
