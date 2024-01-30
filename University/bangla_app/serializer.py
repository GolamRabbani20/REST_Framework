from rest_framework import serializers
from . models import studentInfo
#........................................................................In details......................................................................
class studentInfoSerializer(serializers.Serializer):
    student_name = serializers.CharField(max_length=30)
    student_id = serializers.IntegerField()
    student_dept = serializers.CharField(max_length=50)
    student_phn = serializers.CharField(max_length=15)
    student_age = serializers.FloatField()
    student_sex = serializers.CharField(max_length=10)

    def create(self, validated_data):
        return studentInfo.objects.create(**validated_data)
    
    def update(self, instance, validated_data): # Instance for previous data and validated_data for new data
        instance.student_name = validated_data.get('student_name', instance.student_name)
        instance.student_dept = validated_data.get('student_dept', instance.student_dept)
        instance.student_phn = validated_data.get('student_phn', instance.student_phn)
        instance.student_age = validated_data.get('student_age', instance.student_age)
        instance.student_sex = validated_data.get('student_sex', instance.student_sex)
        instance.save()
        return instance