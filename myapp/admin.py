from django.contrib import admin
from .models import Task
# Register your models here.


class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "is_priority", "is_progress", "is_complete",)
    list_filter = ("is_priority", "is_progress", "is_complete",)


admin.site.register(Task, TaskAdmin)
