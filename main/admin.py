from django.contrib import admin

# Register your models here.
from main.models import ProjectTasks


class ProjectTasksAdmin(admin.ModelAdmin):
    model = ProjectTasks

    list_display = ("name", "complete_percentage")

admin.site.register(ProjectTasks, ProjectTasksAdmin)
