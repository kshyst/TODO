from django.shortcuts import render, redirect

from Todo.forms import AddTaskForm
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

    return render(request , 'index.html' , context)