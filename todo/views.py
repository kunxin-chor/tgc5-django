from django.shortcuts import render, HttpResponse, redirect
from .models import Todo
from .forms import TodoForm


# Create your views here.
def index(request):
    all_todos = Todo.objects.all()
    return render(request, 'todo/index.template.html', {
        'all_todos': all_todos
    })


def create(request):
    # if the method is POST, it means that the form is submitted
    if request.method == 'POST':
        create_form = TodoForm(request.POST)

        # check if all fields are valid
        if create_form.is_valid():
            # if all fields valid, save
            create_form.save()
            return redirect(index)
        else:
            # if there are errors, render again with the form
            # Django will automatically show the errors
            return render(request, 'todo/create.template.html',{
                'form': todo_form
            })
    else:
        todo_form = TodoForm()
        return render(request, 'todo/create.template.html', {
            'form': todo_form
        })