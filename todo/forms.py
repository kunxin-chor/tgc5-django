from django import forms
from .models import Todo, Priority
from pyuploadcare.dj.forms import ImageField


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('name', 'done', 'priority', 'tags', 'image' )


class SearchForm(forms.Form):
    todo_name = forms.CharField(required=False)
    priority = forms.ModelChoiceField(queryset=Priority.objects.all(), required=False)
