from django.contrib import admin

# Register your models here.
from .models import Todo, Priority, Tag


admin.site.register(Todo)
admin.site.register(Priority)
admin.site.register(Tag)
