from django.db import models

# Create your models here.
class studentInfo(models.Model):
    student_name = models.CharField(max_length=30)
    student_id = models.IntegerField()
    student_dept = models.CharField(max_length=50)
    student_phn = models.CharField(max_length=15)
    student_age = models.FloatField()
    student_sex = models.CharField(max_length=10)