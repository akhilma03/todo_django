from django.shortcuts import render,redirect
from .models import Task
from.forms import TodoForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView
from django.urls import reverse_lazy
# Create your views here.

class Tasklistview(ListView):
    model =Task
    template_name = 'todoapp/index.html'
    context_object_name = 'task1'  
    
    
class TaskDetail(DetailView):
    model =Task
    template_name = 'todoapp/details.html'
    context_object_name = 'task' 

class TaskUpdate(UpdateView):
    model =Task
    template_name = 'todoapp/up.html'
    context_object_name = 'task' 
    fields= ('name','priority','date')
    
    def get_success_url(self):
        return reverse_lazy('dhome',kwargs={'pk':self.object.id})
    
class TaskDelete(DeleteView):
    model =Task
    template_name = 'todoapp/delete.html'
    success_url = reverse_lazy('add')  


def add(request):
    task1 = Task.objects.all()
    if request.method == 'POST':
        name= request.POST["task"]
        priority= request.POST["priority"]
        date= request.POST["date"]
        task = Task(name=name,priority=priority,date=date)
        task.save()
    context={"task":task1}    
        
    return render(request,"todoapp/index.html",context )   

def deletes(request,id):
    task =Task.objects.get(id=id)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    return render(request,"todoapp/delete.html")   


def update(request,id):
    task =Task.objects.get(id=id)
    f= TodoForm(request.POST or None,instance=task)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request,"todoapp/edit.html",{'f':f,'task':task})   
         
    
    