from django.shortcuts import render,HttpResponse

# Create your views here.
def task(request):
    return render (request,'todolist.html')

def home(request):
    context={
        
        'pass':"this is base page"
        
    }
    return render (request,'home.html', context)