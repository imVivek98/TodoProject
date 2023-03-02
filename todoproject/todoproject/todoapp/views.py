from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import task
from .forms import TodoForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView

# Create your views here.

class todoListView(ListView):
    model = task
    template_name = 'home.html'
    context_object_name = 'task1'

class todoDetailView(DetailView):
    model = task
    template_name = 'details.html'
    context_object_name = 'i'

class taskUpdate(UpdateView):
    model = task
    template_name = 'update.html'
    context_object_name = 'task1'
    fields = ('name','priority','date')

    def get_success_url(self):
        return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})


class taskDelete(DeleteView):
    model = task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvhome')




def home_pg(request):
    task1 = task.objects.all()
    if request.method == 'POST':
        name = request.POST.get('task','')
        priority = request.POST.get('priority','')
        date = request.POST.get('date','')
        taskinp = task(name=name,priority=priority,date=date)
        taskinp.save()
    return render(request,'home.html',{'task1':task1})


def delete(request,taskid):
    taskdel = task.objects.get(id=taskid)
    if request.method == 'POST':
        taskdel.delete()
        return redirect('/')
    return render(request,'delete.html')


def update(request,id):
    taskup = task.objects.get(id=id)
    f = TodoForm(request.POST or None,instance=taskup)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request,'edit.html',{'f':f,'task':taskup})
