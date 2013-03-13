from django.contrib import admin
from .models import Employee, Dept
from .forms import EmployeeAdminForm


class EmployeeInline(admin.StackedInline):
    form = EmployeeAdminForm
    model = Employee
    extra = 1
    fields = ('name', 'salary', 'word')

class DeptAdmin(admin.ModelAdmin):
    inlines = [EmployeeInline,]
            
admin.site.register(Dept, DeptAdmin)
