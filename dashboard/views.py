from django.contrib.auth.decorators import login_required
from django.shortcuts import render , get_object_or_404 , redirect
from item.models import Items
   
@login_required
def index(request):
    items = Items.objects.filter(created_by=request.user)

    return render(request,'dashboard/Profile.html',{'item':items})


