from django.shortcuts import render,get_object_or_404,redirect
from django.db.models import Q
from .models import Item,Category
from .forms import Newitemform,Edititemform
from django.contrib.auth.decorators import login_required

def items(request):
    query=request.GET.get('query','')
    category_id=request.GET.get('category',0)
    items=Item.objects.filter(is_sold=False)
    categories=Category.objects.all()
    if category_id:
            items=items.filter(category_id=category_id)
    if query:
        items=items.filter(Q(name__icontains=query) | Q(description__icontains=query))
    return render(request,'item/items.html',{
        "items":items,
        "query":query,
        "categories":categories,
        "category_id":int(category_id),
    })
# Create your views here.
def details(request,pk):
    item=get_object_or_404(Item,pk=pk)
    related_items=Item.objects.filter(category=item.category,is_sold=False).exclude(pk=pk)[0:3]
    return render(request,'item/details.html',{
        "item":item,
        "related_items":related_items,
    })
@login_required
def new(request):
    if request.method=='POST':
        forms=Newitemform(request.POST,request.FILES)
        if forms.is_valid():
            item=forms.save(commit=False)
            item.created_by=request.user
            item.save()
            return redirect('items:details',pk=item.id)
    else:
        forms=Newitemform()
    return render(request,'item/form.html',{
        'form':forms,
        'title':'New Item',
    })
@login_required
def delete(request,pk):
    item=get_object_or_404(Item,created_by=request.user,pk=pk)
    item.delete()
    return redirect('dashboard:index')

@login_required
def edit(request,pk):
    item=get_object_or_404(Item,created_by=request.user,pk=pk)
    if request.method=='POST':
        forms=Edititemform(request.POST,request.FILES,instance=item)
        if forms.is_valid():
            item.save()
            return redirect('items:details',pk=item.id)
    else:
        forms=Edititemform(instance=item)
    return render(request,'item/form.html',{
        'form':forms,
        'title':'Edit Item',
    })