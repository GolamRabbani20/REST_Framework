from django.contrib import admin
from . models import teacherInfo, courses, studentInfo_DataScience
# Register your models here.

@admin.register(teacherInfo)
class teacherAdmin(admin.ModelAdmin):
    list_display = ['id', 'teacher_name', 'dept_name', 'teacher_age', 'teacher_email']

@admin.register(courses)
class courseAdmin(admin.ModelAdmin):
    list_display = ['course_id', 'course_name', 'credit', 'course_fee']

@admin.register(studentInfo_DataScience)
class DS_studentInfoAdmin(admin.ModelAdmin):
    list_display = ['student_id', 'student_name', 'student_dept', 'course_id' ]
