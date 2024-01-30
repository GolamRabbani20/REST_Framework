from rest_framework import serializers
from . models import teacherInfo, courses, studentInfo_DataScience

class teacherInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = teacherInfo
        fields = ['teacher_name', 'dept_name', 'teacher_age', 'teacher_email']

class courseSerializer(serializers.ModelSerializer):
    class Meta:
        model = courses
        fields = ['course_id', 'course_name', 'credit', 'course_fee']
    
class DS_studentInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = studentInfo_DataScience
        fields = ['pk', 'student_id', 'student_name', 'student_dept', 'course_id']