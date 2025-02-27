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

from Todo.views import todo_home , update_todo , delete_todo , create_todo

urlpatterns = [
        path('admin/', admin.site.urls),
        path("", view=todo_home, name="home_todo"),
        path("update/<int:id>/" , view=update_todo , name="update_todo"),
        path("delete/<int:id>/" , view=delete_todo , name="delete_todo"),
        path("create/" , view=create_todo , name="create_todo")
]
