from django.db import models

# Create your models here.


# This class represents the Todo table in the database
# Todo will inherit from models.Model; the latter is a Django class
# that already has the funcitonality we need. By inheriting, Todo will
# have all those functionalities
class Todo(models.Model):
    name = models.CharField(max_length=255, blank=False)
    done = models.BooleanField(blank=False, default=False)
    priority = models.ForeignKey('Priority', on_delete=models.PROTECT)
    tags = models.ManyToManyField('Tag', blank=True)

    def __str__(self):
        return self.name


class Priority(models.Model):
    name = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.name