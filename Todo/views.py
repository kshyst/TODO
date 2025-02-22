from django.shortcuts import render

from Todo.models import Todo


# Create your views here.

def todo_index(request):
    context = {
        "todos" : Todo.objects.all()
    }

    return render(request , 'index.html' , context)