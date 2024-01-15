from django.shortcuts import render , redirect
from item.models import Items , Category
from django.contrib.auth import logout as logl
from .forms import SignUpform
# Create your views here.

def index(request):
    items = Items.objects.filter(is_sold=False)
    category = Category.objects.all()
    return render(request,'core/index.html',{"category":category,"item":items})

def contact(request):
    return render(request,"core/contact.html")

def browse(request):
    items = Items.objects.filter(is_sold=False)
    category = Category.objects.all()
    return render(request,'main/browse.html',{"category":category,"item":items})

def home(request):
    return render(request,'main/home.html',{})

def logout(request):
    if request.user.is_authenticated:
        logl(request)
        return render(request,'core/logout.html')
    else:
        return redirect("/")

def signup(request):
    if request.method=="POST":
        form = SignUpform(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = SignUpform()

    return render(request,'core/signup.html',{"form":form})