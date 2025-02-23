from django.shortcuts import render, redirect

from Todo.forms import AddTaskForm, UpdateTaskForm
from Todo.models import Todo


# Create your views here.

def todo_index(request):
    context = {
        "todos" : Todo.objects.all(),
        "form" : AddTaskForm()
    }

    if request.method == "POST" :
        form = AddTaskForm(request.POST)

        if form.is_valid():
            form.save()

        return redirect('/')

    return render(request , 'index.html' , context=context)

def update_todo(request , id):

    context = {
        'id' : id,
        'form' : UpdateTaskForm()
    }

    if request.method == "POST" :

        form = UpdateTaskForm(request.POST)

        if form.is_valid():
            form.update(id)
            return redirect('/')

    return render(request , 'update.html' , context=context)

def delete_todo(request , id):
    if Todo.objects.get(id = id) is not None:
        Todo.objects.get(id=id).delete()

    return redirect('/')