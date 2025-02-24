from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views import View
from django.views.generic import CreateView, ListView, DeleteView, UpdateView

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

class UpdateTodo(UpdateView):
    model = Todo

    fields = ['name' , 'due_date' , 'checked']

    def get_success_url(self):
        return reverse('home_todo')

class DeleteTodo(DeleteView):
    model = Todo

    def get_success_url(self):
        return reverse('home_todo')

class CreateTodo(CreateView):
    model = Todo
    form_class = TaskForm

    def get_success_url(self):
        return reverse('home_todo')

