from django.contrib import admin
from .models import Employee, Type, JobTemplate, JobInstance

# Register your models here.

admin.site.register(JobTemplate)
admin.site.register(Employee)
admin.site.register(Type)
admin.site.register(JobInstance)
