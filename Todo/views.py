from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views import View
from django.views.generic import CreateView, ListView, DeleteView

from Todo.forms import TaskForm
from Todo.models import Todo


# Create your views here.

class TodoIndex(View):

    def get(self , request):
        return render(request , 'index.html' , context={
            "todos" : Todo.objects.all(),
            "form" : TaskForm(),
        })

class RetrieveTodo(ListView):
    model = Todo

def update_todo(request , id):

    todo = get_object_or_404(Todo , id=id)

    context = {
        'id' : id,
        'form' : TaskForm(),
        'name' : todo.name,
        'date' : todo.due_date,
        'checked' : todo.checked
    }

    if request.method == "POST" :

        form = TaskForm(request.POST , instance=todo)

        if form.is_valid():
            form.save()
            return redirect("home_todo")

    return render(request , 'update.html' , context=context)

def delete_todo(request , id):
    obj = Todo.objects.get(id = id)
    if obj:
        obj.delete()
    return redirect("home_todo")

class DeleteTodo(DeleteView):
    model = Todo

    def get_success_url(self):
        return reverse('home_todo')

class CreateTodo(CreateView):
    model = Todo
    form_class = TaskForm

    def get_success_url(self):
        return reverse('home_todo')

