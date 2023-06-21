from django.contrib import admin
from .models import Task
# Register your models here.


class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ("created",)


# registrar aqui para ver las tablas en el administrador
admin.site.register(Task, TaskAdmin)
