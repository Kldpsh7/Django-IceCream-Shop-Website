from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('<h1>Welcome to homepage</h1>')

def about(request):
    return HttpResponse('<h1> This is about page</h1>')

def services(request):
    return HttpResponse('<h1>This is services page</h1>')

def contact(request):
    return HttpResponse('<h1>This is contact page</h1>')