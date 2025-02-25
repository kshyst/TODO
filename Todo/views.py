from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.views.generic import CreateView, ListView, DeleteView, UpdateView

from Todo.forms import TaskForm, SearchForm
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
    ordering = 'due_date'

    def get_queryset(self):
        queryset = super().get_queryset()
        search_form = SearchForm(self.request.GET)

        if search_form.is_valid():
            search_text = search_form.cleaned_data.get('search_text')
            if search_text:
                queryset = queryset.filter(Q(name__icontains=search_text))

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = SearchForm(self.request.GET)
        return context

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

