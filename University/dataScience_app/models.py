from django.db import models

# Create your models here.
class teacherInfo(models.Model):
    teacher_name = models.CharField(max_length=30)
    dept_name = models.CharField(max_length=50)
    teacher_age = models.IntegerField()
    teacher_email = models.CharField(max_length=50)

class studentInfo_DataScience(models.Model):
    student_id = models.IntegerField()
    student_name = models.CharField(max_length=25)
    student_dept = models.CharField(max_length=20)
    course_id = models.CharField(max_length=10)

class courses(models.Model):
    course_id = models.CharField(max_length= 12)
    course_name = models.CharField(max_length= 30)
    credit = models.IntegerField()
    course_fee = models.IntegerField()

