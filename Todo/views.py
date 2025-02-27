from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from Todo.forms import TaskForm
from Todo.models import Todo


# Create your views here.

def todo_home(request):
    context = {
        "todos" : Todo.objects.all(),
        "form" : TaskForm(),
    }

    return render(request , 'index.html' , context=context)

def update_todo(request , id):

    todo = get_object_or_404(Todo , id=id)

    context = {
        'id' : id,
        'form' : TaskForm(initial={
            'name' : todo.name,
            'due_date' : todo.due_date,
            'checked' : todo.checked
        }),
    }

    if request.method == "POST" :

        form = TaskForm(request.POST , instance=todo)

        if form.is_valid():
            form.save()
            return redirect("home_todo")
        else:
            return render(request, 'update.html', context={"form": form})

    return render(request , 'update.html' , context=context)

def delete_todo(request , id):
    obj = Todo.objects.get(id = id)
    if obj:
        obj.delete()
    return redirect("home_todo")

def create_todo(request):
    context = {'form' : TaskForm()}

    if request.method == "POST" :
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home_todo")
        else:
            return render(request, 'create.html', context={"form":form})

    return render(request , 'create.html' , context=context)
