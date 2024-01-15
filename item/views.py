from django.shortcuts import render , HttpResponse , redirect , get_object_or_404
from .models import Items
from django.contrib.auth.decorators import login_required

#to use the premade form made by django , we gave the field we want in the this form
from .forms import NewItemForm,EditItemForm

# Create your views here.
def detail(request,pk):
    item =  Items.objects.get(pk=pk)
    if item is None:
        return HttpResponse(status_code=404)
    else:
        releated_items = Items.objects.filter(category = item.category , is_sold=False).exclude(pk=pk)[:3]
        return render(request,'item/detail.html',{"item":item , "related_items":releated_items})
    
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

            return redirect(f'/item/{item.id}' , pk=item.id)
    else:
        form = NewItemForm()
    return render(request,'item/form.html',{'form':form,'title':'New Item'})

    
@login_required
def edit(request,pk):
    item = get_object_or_404(Items,pk=pk, created_by=request.user )
    if request.method== 'POST':
        #passed the information to form class django will auto verify it 
        form= EditItemForm(request.POST , request.FILES,instance=Items)

        if form.is_valid():
            item.save()

            return redirect(f'/item/{item.id}' , pk=item.id)
    else:
        form = EditItemForm(instance=Items)
    return render(request,'item/form.html',{'form':form,'title':'Edit Item'})

@login_required
def delete_item(request ,pk):
    item = get_object_or_404(Items,pk=pk, created_by=request.user)
    item.delete()

    return redirect("/dashboard")