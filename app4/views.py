from django.shortcuts import render #HttpResponse
from .models import user


# Create your views here.
def index(request):
    return render(request,"index.html")
def about(request):
    return render(request,"about.html")
def gallery(request):
    return render(request,"gallery.html")
def contact(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        message=request.POST['message']
        a = user(Name=name,Email=email,Subject=subject,Message=message)
        a.save()
    return render(request,"contact.html")
def service(request):
    return render(request,"service.html")
def product(request):
    return render(request,"product.html")