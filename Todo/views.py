from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from django.views import View
from rest_framework import viewsets, permissions, authentication
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

from Todo.forms import TaskForm, SearchForm, RegisterForm, LoginForm
from Todo.models import Todo
from Todo.serializers import UserSerializer, TodoSerializer


class RetrieveTodo(ListView):
    model = Todo
    ordering = "due_date"
    login_url = reverse_lazy("home_todo")

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


@method_decorator([login_required(login_url=reverse_lazy("login_todo"))], "get")
@method_decorator([login_required(login_url=reverse_lazy("login_todo"))], "post")
class UpdateTodo(UpdateView):
    model = Todo

    fields = ["name", "due_date", "checked"]

    def post(self, request, *args, **kwargs):
        pk = int(kwargs.get('pk'))
        if not Todo.objects.get(pk = pk).users.contains(request.user):
            self.object = self.get_object()
            return self.form_invalid(self.get_form())

        return super().post(request , *args , **kwargs)

    def get_success_url(self):
        return reverse("home_todo")


class DeleteTodo(LoginRequiredMixin ,DeleteView):
    model = Todo
    login_url = reverse_lazy("login_todo")

    def post(self, request, *args, **kwargs):
        pk = int(kwargs.get('pk'))
        if not Todo.objects.get(pk = pk).users.contains(request.user):
            self.object = self.get_object()
            return self.form_invalid(self.get_form())

        return super().post(request , *args , **kwargs)

    def get_success_url(self):
        return reverse_lazy("home_todo")


class CreateTodo(LoginRequiredMixin, CreateView):
    model = Todo
    form_class = TaskForm
    login_url = reverse_lazy("login_todo")

    def get_success_url(self):
        return reverse("home_todo")

    def form_valid(self, form):
        task = form.save(commit=False)
        task.save()
        task.users.clear()
        task.users.add(self.request.user)
        return super().form_valid(form)


class SignUpTodo(CreateView):
    model = User
    form_class = RegisterForm

    def get_success_url(self):
        return reverse_lazy("home_todo")

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["menu_name"] = "Signup Menu"

        return context


class LoginTodo(LoginView):
    form_class = LoginForm
    template_name = "auth/user_form.html"

    def get_success_url(self):
        return reverse_lazy("home_todo")

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["menu_name"] = "Login Menu"

        return context


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


class ShareTodoConfirm(LoginRequiredMixin ,View):
    login_url = reverse_lazy('login_todo')

    def get(self, request, pk, username):
        selected_todo = Todo.objects.get(id=int(pk))

        if self.request.user not in selected_todo.users.all():
            return redirect(
                "share-todo",
                pk,
            )

        selected_todo.users.add(User.objects.get(username__exact=username))

        return redirect("home_todo")

"""
API Views
"""

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


@csrf_exempt
def show_todo_list(request):
    if request.method == "GET":
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = TodoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

