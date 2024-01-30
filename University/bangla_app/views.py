from django.shortcuts import render
from django.views import View
#Serializer
from . serializer import studentInfoSerializer
from . models import studentInfo
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
#Deserializer
from django.views.decorators.csrf import csrf_exempt
import io
from rest_framework.parsers import JSONParser

#-----------------------------------------------------------In details--------------------------------------------------------------------------
def welcome_msg(request):
    return render(request, 'bangla/bangla.html')

class bangla_info(View):
    def get(self, request):
        return render(request, 'bangla/bng.html')

#Queryset => For RETRIVE data to User    
def student_Info(request):
    #complex data
    student_data = studentInfo.objects.all()
    #Complex to Pythod dict
    python_dict = studentInfoSerializer(student_data, many=True)
    #Python to Json
    json_data =  JSONRenderer().render(python_dict.data)
    # Json send to user
    return HttpResponse(json_data, content_type = 'application/json')

#Student Instance    
def student_Instance(request, pk):
    #complex data
    student_data = studentInfo.objects.get(id= pk)
    #Complex to Pythod dict
    python_dict = studentInfoSerializer(student_data)
    #Python to Json
    json_data =  JSONRenderer().render(python_dict.data)
    #Json send to user
    return HttpResponse(json_data, content_type = 'application/json')

#For INSERTING/UPDATING/DELETING data => Deserialize process
@csrf_exempt
def studentInfo_create(request):
    #For INSERTING data
    if request.method == 'POST': 
        json_data = request.body
        stream = io.BytesIO(json_data)
        #stream to python
        python_dict = JSONParser().parse(stream)
        #Python to complex 
        complex_data = studentInfoSerializer(data = python_dict)
        if complex_data.is_valid():
            complex_data.save()
            message = {'msg': 'Data inserted successfully!'}
            json_msg = JSONRenderer().render(message)
            return HttpResponse(json_msg, content_type = 'application/json')
        json_msg = JSONRenderer().render(complex_data.errors)
        return HttpResponse(json_msg, content_type='application/json')
    
#For UPDATEING data
    if request.method == 'PUT':
        json_data = request.body
        #json to stream 
        stream = io.BytesIO(json_data)
        #stream to python dict
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('student_id')
        std = studentInfo.objects.get(student_id = id)
        serializer = studentInfoSerializer(std, data = pythondata, partial=True)
        if serializer.is_valid():
            serializer.save()
            msg = {'Data updated successfully!'}
            json_msg = JSONRenderer().render(msg)
            return HttpResponse(json_msg, content_type = 'application/json')
        json_msg = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_msg, content_type = 'application/json')
    
#For DELETING data
    if request.method == "DELETE":
        #print("request:",request)
        json_data = request.body
        #print("json_data_r:",json_data)
        #print('json_data type:', type(json_data))
        #Json to Stream
        stream = io.BytesIO(json_data)
        #print("stream:",stream)
        #Stream to Python dict
        python_dict =  JSONParser().parse(stream)
        #print("python_dict:",python_dict)
        id = python_dict.get('student_id')
        #print('ID:', id)
        st_data = studentInfo.objects.get(student_id = id)
        #print('st_data:', st_data)
        #print('st_data type:', type(st_data))
        st_data.delete()
        msg = {"Data deleted successfully"}
        json_msg = JSONRenderer().render(msg)
        #print('json_msg:', json_msg)
        return HttpResponse(json_msg, content_type = 'application.json')
