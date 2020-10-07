from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import View
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import permission_required
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission, User, PermissionManager
from .models import Task
# Create your views here.


# @permission_required('myapp.view_task', raise_exception=True)
def tasks(request):
    tasks = Task.objects.all()
    content_type = ContentType.objects.get_for_model(Task)
    permissions = Permission.objects.filter(content_type=content_type)
    context = {
        "tasks": tasks,
        "permissions": permissions
    }
    return render(request, "myapp/tasks.html", context)


def move_task_to_priority(request, id):
    task = Task.objects.get(id=id)
    task.is_priority = True
    if task.is_progress or task.is_complete:
        task.is_progress = False
        task.is_complete = False
    task.save()
    return JsonResponse({"message": "Task added to the Priority card"})


def move_task_to_progress(request, id):
    task = Task.objects.get(id=id)
    task.is_progress = True
    if task.is_complete or task.is_priority:
        task.is_priority = False
        task.is_complete = False
    task.save()
    return JsonResponse({"message": "Task added to the in-progress card"})


def move_task_to_complete(request, id):
    task = Task.objects.get(id=id)
    task.is_complete = True
    if task.is_priority or task.is_progress:
        task.is_progress = False
        task.is_priority = False
    task.save()
    return JsonResponse({"message": "Task added to the Complete card"})
