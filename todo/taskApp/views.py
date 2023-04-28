from django.shortcuts import render, redirect
from .models import *
from .forms import taskForm

# Create your views here.
def index(request):
    task = taskModel.objects.all 
    form = taskForm()
    
    if request.method == 'POST':
        form = taskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
        
    task_dict = {
        'tasks' : task,
        'forms' : form,
    }
    return render(request, 'todo/todo.html', context=task_dict)

def deleteTask(request, id):
    task = taskModel.objects.get(id=id)
    task.delete() 
    return redirect('/')

def updateTask(request, id):
    task = taskModel.objects.get(id=id)
    form = taskForm(instance=task)
    
    if request.method == 'POST':
        form = taskForm(request.POST, instance=task)
        if form.is_valid:
            form.save()
            return redirect('/')
    
    context = {
        'form' : form,
    }
    
    return render(request, 'todo/update.html', context=context)


def completed(requests, id):
    task = taskModel.objects.get(id=id)
    task.complete = True 
    task.save()
    return redirect('/')

def notCompleted(requests, id):
    task1 = taskModel.objects.get(id=id)
    task1.complete = False  
    task1.save()
    return redirect('/')