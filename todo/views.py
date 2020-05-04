from django.shortcuts import render, HttpResponse
from .models import Todo


# Create your views here.
def index(request):
    all_todos = Todo.objects.all()
    return render(request, 'todo/index.template.html', {
        'all_todos':all_todos
    })
