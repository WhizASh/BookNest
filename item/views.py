from django.shortcuts import render , HttpResponse , redirect , get_object_or_404
from .models import Items , Category
from django.contrib.auth.decorators import login_required


# to search in multiple filed (book name & description or by price etc)
from django.db.models import Q

#to use the premade form made by django , we gave the field we want in the this form
from .forms import NewItemForm,EditItemForm

# Create your views here.
def old_detail(request,pk):
    item =  Items.objects.get(pk=pk)
    if item is None:
        return HttpResponse(status_code=404)
    else:
        releated_items = Items.objects.filter(category = item.category , is_sold=False).exclude(pk=pk)[:3]
        return render(request,'item/detail.html',{"item":item , "related_items":releated_items})
    
def detail(request,pk):
    item =  Items.objects.get(pk=pk)
    if item is None:
        return HttpResponse(status_code=404)
    else:
        releated_items = Items.objects.filter(category = item.category , is_sold=False).exclude(pk=pk)[:3]
        return render(request,'item/Bookinfo.html',{"item":item , "related_items":releated_items})
    
@login_required
def new(request):
    if request.method== 'POST':
        #passed the information to form class django will auto verify it 
        form= NewItemForm(request.POST , request.FILES)

        if form.is_valid():
            #commit false cause created_by will not be save so might  generate error
            item = form.save(commit=False)      
            item.created_by=request.user
            item.save()

            return redirect(f'/item/browse/{item.id}' , pk=item.id)
    else:
        form = NewItemForm()
    return render(request,'item/Add_item.html',{'form':form,'title':'New Item'})

    
@login_required
def edit(request,pk):
    item = get_object_or_404(Items,pk=pk, created_by=request.user )
    if request.method== 'POST':
        #passed the information to form class django will auto verify it 
        form= EditItemForm(request.POST , request.FILES,instance=item)

        if form.is_valid():
            item.save()

            return redirect(f'/item/browse/{item.id}' , pk=item.id)
    else:
        form = EditItemForm(instance=item)
    return render(request,'item/edit_item.html',{'form':form,'title':'Edit Item'})

@login_required
def delete_item(request ,pk):
    item = get_object_or_404(Items,pk=pk, created_by=request.user)
    item.delete()

    return redirect("/dashboard")   


def browse(request):
    items = Items.objects.filter(is_sold=False)
    categories = Category.objects.all()
    #to know which category has been selected 
    category_id = request.GET.get('category' , 0)
    #default value ('') so that it own't display None every time reloaded page 
    query = request.GET.get('query','')

    if category_id:
        items = items.filter(category_id=category_id)

    if query:
        #search for book_name case insensitively (__icontains will do case insensitively)
        items = items.filter(Q(book_name__icontains=query) | Q(description__icontains=query) | Q(publication__icontains=query))

    return render(request,'item/browse.html',{'item':items,'query':query , 'categories':categories ,'category_id':int(category_id)})

def old_browse(request):
    items = Items.objects.filter(is_sold=False)
    categories = Category.objects.all()
    #to know which category has been selected 
    category_id = request.GET.get('category' , 0)
    #default value ('') so that it own't display None every time reloaded page 
    query = request.GET.get('query','')

    if category_id:
        items = items.filter(category_id=category_id)

    if query:
        #search for book_name case insensitively (__icontains will do case insensitively)
        items = items.filter(Q(book_name__icontains=query) | Q(description__icontains=query) | Q(publication__icontains=query))

    return render(request,'item/item.html',{'item':items,'query':query , 'categories':categories ,'category_id':int(category_id)})