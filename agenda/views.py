from django.shortcuts import render,HttpResponse,redirect
from agenda.models import Task
from django.contrib import messages
from agenda.forms import TaskForm
# Create your views here.
def task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        messages.success(request,"New task added successfully")
        return redirect('task')
    else:
        task = Task.objects.all()
        return render(request, 'todolist.html', {'task': task})
def home(request):
    context={
        
        'pass':"this is base page"
        
    }
    return render (request,'home.html', context)