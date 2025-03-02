"""
URL configuration for ToDoList project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path

from Todo.views import (
    CreateTodo,
    RetrieveTodo,
    DeleteTodo,
    UpdateTodo,
    SignUpTodo,
    LoginTodo,
    LogoutTodo,
    ShareTodo,
    ShareTodoConfirm,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", view=RetrieveTodo.as_view(), name="home_todo"),
    path("update/<int:pk>/", view=UpdateTodo.as_view(), name="update_todo"),
    # path("delete/<int:id>/" , view=delete_todo , name="delete_todo"),
    path("<pk>/delete/", view=DeleteTodo.as_view(), name="delete_todo"),
    path("create/", view=CreateTodo.as_view(), name="create_todo"),
    path("signup/", view=SignUpTodo.as_view(), name="signup_todo"),
    path("login/", view=LoginTodo.as_view(), name="login_todo"),
    path("logout/", view=LogoutTodo.as_view(), name="logout_todo"),
    path("share/<pk>", view=ShareTodo.as_view(), name="share-todo"),
    path(
        "share/<pk>/<username>",
        view=ShareTodoConfirm.as_view(),
        name="share-todo-confirm",
    ),
]
