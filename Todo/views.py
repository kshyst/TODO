from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from django.views import View

from Todo.forms import TaskForm, SearchForm, RegisterForm, LoginForm
from Todo.models import Todo


# @method_decorator(login_required, name="dispatch")
class RetrieveTodo(ListView):
    model = Todo
    ordering = "due_date"

    # def get(self, request, *args, **kwargs):
    #     print(request.GET.keys().__str__())
    #
    #     return super().get(request , *args , **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()

        queryset = queryset.filter(Q(users__username=self.request.user.username))

        search_form = SearchForm(self.request.GET)

        if search_form.is_valid():
            search_text = search_form.cleaned_data.get("search_text")
            if search_text and search_text != " ":
                queryset = queryset.filter(Q(name__icontains=search_text))

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if s := SearchForm(self.request.GET):
            context["search"] = s

        if self.request.user.is_authenticated:
            context["username"] = self.request.user.username

        return context


class UpdateTodo(UpdateView):
    model = Todo

    fields = ["name", "due_date", "checked"]

    def get_success_url(self):
        return reverse("home_todo")


class DeleteTodo(DeleteView):
    model = Todo

    def get_success_url(self):
        return reverse_lazy("home_todo")


class CreateTodo(CreateView):
    model = Todo
    form_class = TaskForm

    def get_success_url(self):
        return reverse("home_todo")

    def form_valid(self, form):
        task = form.save(commit=False)
        task.save()  # Save the task first
        task.users.clear()  # Remove any existing relationships
        task.users.add(self.request.user)  # Assign the user
        return super().form_valid(form)


class SignUpTodo(CreateView):
    model = User
    form_class = RegisterForm

    def get_success_url(self):
        return reverse_lazy("home_todo")


class LoginTodo(LoginView):
    form_class = LoginForm
    template_name = "auth/user_form.html"

    def get_success_url(self):
        return reverse_lazy("home_todo")


class LogoutTodo(LogoutView):
    def get_success_url(self):
        return reverse_lazy("home_todo")

    def get_redirect_url(self):
        return reverse_lazy("home_todo")


class ShareTodo(ListView):
    model = User
    ordering = "username"
    template_name = "Todo/todo_list_share.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["users"] = User.objects.all().exclude(
            username__exact=self.request.user.username
        )
        url = self.request.path.split("/")
        context["task_name"] = (
            Todo.objects.all().filter(id=int(url[len(url) - 1]))[0].name
        )
        context["task_id"] = int(url[len(url) - 1])
        return context


@method_decorator(login_required, name="get")
class ShareTodoConfirm(View):
    def get(self, request, pk, username):
        selected_todo = Todo.objects.get(id=int(pk))

        if self.request.user not in selected_todo.users.all():
            return redirect(
                "share-todo",
                pk,
            )

        selected_todo.users.add(User.objects.get(username__exact=username))

        return redirect("home_todo")
