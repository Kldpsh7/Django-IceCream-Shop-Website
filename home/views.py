from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    context={
        'variable':'This is a variable'
    }
    #return HttpResponse('<h1>Welcome to homepage</h1>')
    return render(request,'index.html',context)

def about(request):
    #return HttpResponse('<h1> This is about page</h1>')
    return render(request,'about.html')

def services(request):
    #return HttpResponse('<h1>This is services page</h1>')
    return render(request,'services.html')

def contact(request):
    #return HttpResponse('<h1>This is contact page</h1>')
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        
        contact=Contact(name=name,email=email,phone=phone,date=datetime.today())
        contact.save()
        messages.success(request,'Contact form submitted successfully')
    return render(request,'contact.html')