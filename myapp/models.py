from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Project(models.Model):
    project_name = models.CharField(
        max_length=30, blank=False, null=False, verbose_name="Project Name")
    project_owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="project_owner", verbose_name="Project Owner")

    project_users = models.ManyToManyField(User, verbose_name="Project Users")
    project_description = models.TextField(verbose_name="Project Description")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=False)


class Task(models.Model):
    title = models.CharField(max_length=30, blank=False, null=False)
    description = models.TextField()

    is_priority = models.BooleanField(default=False)
    is_progress = models.BooleanField(default=False)
    is_complete = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"
