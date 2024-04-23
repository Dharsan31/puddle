from django.shortcuts import render
from items.models import Category,Item
from . forms import SignupForm
# Create your views here.
def index(request):
    items=Item.objects.filter(is_sold=False)[0:6]
    categories=Category.objects.all()
    return render(request,'core/index.html',{
        'categories':categories,
        'items':items,
    })
def contact(request):
    return render(request,'core/contacts.html')
def Signup(request):
    form=SignupForm()
    return render(request,'core/Signup.html',{
        "form":form
    })