from django.contrib import admin
from . models import studentInfo 
# Register your models here.
@admin.register(studentInfo)
class studentAdmin(admin.ModelAdmin):
    list_display = ['student_id', 'student_name', 'student_dept', 'student_phn', 'student_age', 'student_sex']