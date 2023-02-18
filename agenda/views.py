from django.shortcuts import render,HttpResponse,redirect
from agenda.models import Task
from django.contrib import messages
from agenda.forms import TaskForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    context={
        
        'pass':"this is base page"
        
    }
    return render (request,'home.html', context)

@login_required
def task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():          
           form.save()#this task is used for only vlaid user who save the task they are only allowed to see that
        messages.success(request,"New task added successfully")
        return redirect('task')
    else:
        task = Task.objects.order_by('id') #this should get the display all item according to order ascending 
    # this is for pagination purposes
        paginator = Paginator(task, 5)
        page_number = request.GET.get('page')
        task = paginator.get_page(page_number)
       #making page number in visible 5 range
        context={
            'task': task,
            
        }
        return render(request, 'todolist.html',context)
# this funciton is used to marks the incompleted task as compted task
@login_required
def as_completed(request,task_id):
    task=Task.objects.get(pk=task_id)
    task.status=True
    task.save()
    return redirect('task')
# this fucntion is used to make the compled task as Incomplete 
@login_required
def as_incompleted(request,task_id):
    task=Task.objects.get(pk=task_id)
    task.status=False
    task.save()
    return redirect('task')
# this is used to delete a task
@login_required
def deleted(request,task_id):
    task=Task.objects.get(pk=task_id)
    task_name=task.Task_name
    task.delete()
    messages.success(request,task.Task_name + ' - deleted successfully')
    return redirect('task')

# this is used to edit the task list 
@login_required
def edit_task(request,task_id):
    if request.method == 'POST':
        task=Task.objects.get(pk=task_id)
        form=TaskForm(request.POST or None ,instance=task)
        task_name=task.Task_name
        if form.is_valid():
            form.save()
        messages.success(request,task_name + ' - Updated Successfully ')
        return redirect('task')
    else:
        task=Task.objects.get(pk=task_id)
        return render(request,'edit.html',{'task_obj':task})

@login_required
def contact(request):
    context={
        'greet':"welcome to Contact-page"
    }
    return render(request, 'contact.html',context)
@login_required
def about(request):
    context={
        'greet':"welcome to about-page"
    }
    return render(request, 'about.html',context)