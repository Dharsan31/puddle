from django.shortcuts import render,redirect
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
    if request.method=='POST':
        form=SignupForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
     form=SignupForm()
    return render(request,'core/Signup.html',{
        "form":form
    })
def about(request):
    return render(request,'core/about.html')
def terms(request):
    return render(request,'core/terms.html')
def policies(request):
    return render(request,'core/policy.html')