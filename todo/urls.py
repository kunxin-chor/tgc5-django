
from django.contrib import admin
from django.urls import path, include
import todo.views

urlpatterns = [
    path('', todo.views.index, name='view_todo_route'),
    path('add_todo', todo.views.create),
    path('update_todo/<todo_id>', todo.views.update_todo, name='update_todo_route'),
    path('delete_todo/<todo_id>', todo.views.delete_todo, name='delete_todo_route')
]
