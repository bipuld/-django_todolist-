from django.shortcuts import render,HttpResponse

# Create your views here.
def task_home(request):
    context={
        
        'pass':"this is base page"
        
    }
    return render (request,'base.html', context)