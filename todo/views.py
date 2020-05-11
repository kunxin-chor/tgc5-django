from django.shortcuts import render, HttpResponse, redirect, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from .models import Todo
from .forms import TodoForm, SearchForm
from django.db.models import Q


# Create your views here.
def index(request):
    # all_todos = Todo.objects.all()
    # all_todos = all_todos.filter(user=request.user)
    # all_todos = all_todos.filter(done=True)
    # all_todos = all_todos.filter(priority__name__in=['High','Low'])
    # all_todos = all_todos.filter(name__icontains="letters")

    all_todos = Todo.objects.filter(user=request.user)
    search_form = SearchForm(request.GET)

    # create a query that is always true
    queries = ~Q(pk__in=[])

    if request.GET:
        if 'todo_name' in request.GET and request.GET['todo_name']:
            queries = queries & Q(name__icontains=request.GET['todo_name'])

        if 'priority' in request.GET and request.GET['priority']:
            queries = queries & Q(priority__in=request.GET['priority'])

    all_todos = all_todos.filter(queries)

    print(all_todos.query)
    return render(request, 'todo/index.template.html', {
        'all_todos': all_todos,
        'search_form': search_form
    })


@login_required
def create(request):
    # if the method is POST, it means that the form is submitted
    if request.method == 'POST':
        create_form = TodoForm(request.POST)

        # check if all fields are valid
        if create_form.is_valid():
            # if all fields valid, save

            # create the instance BUT don't save to database yet
            saved_todo = create_form.save(commit=False)
      
            # assign the current logged in user to the todo that we just created
            saved_todo.user = request.user
            saved_todo.save()

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