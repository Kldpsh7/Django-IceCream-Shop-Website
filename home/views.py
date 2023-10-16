from django.shortcuts import render,HttpResponse

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
    return render(request,'contact.html')