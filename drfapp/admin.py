from django.contrib import admin
from .models import  Employee
# Register your models here.
class Employeeadmin(admin.ModelAdmin):

    list_display = ['id','eno','ename','esal','eaddress']

admin.site.register(Employee)


