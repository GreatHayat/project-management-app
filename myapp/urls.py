from django.urls import path
from . import views

urlpatterns = [
    path("", views.tasks, name="tasks"),
    path("update-task-priority/<int:id>",
         views.move_task_to_priority, name="update-task-priority"),
    path("update-task-progress/<int:id>",
         views.move_task_to_progress, name="update-task-progress"),
    path("update-task-complete/<int:id>",
         views.move_task_to_complete, name="update-task-complete"),
]
