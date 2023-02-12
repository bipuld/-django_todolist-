from django.shortcuts import render,HttpResponse,redirect
from agenda.models import Task
from django.contrib import messages
from agenda.forms import TaskForm
from django.core.paginator import Paginator
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
    # this is for pagination purposes
        paginator = Paginator(task, 5)
        page_number = request.GET.get('page')
        task = paginator.get_page(page_number)
       #making page number in visible 5 range
        context={
            'task': task,
            
        }
        return render(request, 'todolist.html',context)
def home(request):
    context={
        
        'pass':"this is base page"
        
    }
    return render (request,'home.html', context)