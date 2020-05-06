from django.shortcuts import render, HttpResponse, redirect, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from .models import Todo
from .forms import TodoForm


# Create your views here.
def index(request):
    all_todos = Todo.objects.all()
    return render(request, 'todo/index.template.html', {
        'all_todos': all_todos
    })


@login_required
def create(request):
    # if the method is POST, it means that the form is submitted
    if request.method == 'POST':
        create_form = TodoForm(request.POST)

        # check if all fields are valid
        if create_form.is_valid():
            # if all fields valid, save
            saved_todo = create_form.save()
            messages.success(request, f"Todo '{saved_todo.name}' has been added successfully!")
            return redirect(index)
        else:
            # if there are errors, render again with the form
            # Django will automatically show the errors
            return render(request, 'todo/create.template.html', {
                'form': create_form
            })
    else:
        todo_form = TodoForm()
        return render(request, 'todo/create.template.html', {
            'form': todo_form
        })


def update_todo(request, todo_id):
    # means: get a Todo which primary key matches todo_id
    todo = get_object_or_404(Todo, pk=todo_id)

    if request.method == 'POST':
        todo_form = TodoForm(request.POST, instance=todo)
        if todo_form.is_valid():
            todo_form.save()
            return redirect(reverse(index))
        else:
            return render(request, 'todo/update.template.html', {
                'form': todo_form
            })

    todo_form = TodoForm(instance=todo)
    return render(request, 'todo/update.template.html', {
        'form': todo_form
    })


def delete_todo(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)

    if request.method == "POST":
        messages.success(request, f"Todo '{todo.name}' has been deleted")   
        todo.delete()
        return redirect(reverse(index))
    else:
        return render(request, 'todo/delete.template.html', {
            'todo': todo
        })