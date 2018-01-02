from django.contrib import admin
from .models import Employee, Type, Operation, Task

# Register your models here.

admin.site.register(Operation)
admin.site.register(Employee)
admin.site.register(Type)
admin.site.register(Task)
