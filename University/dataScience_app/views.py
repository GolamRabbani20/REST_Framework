from .models import teacherInfo, courses, studentInfo_DataScience
from .serializers import teacherInfoSerializer, courseSerializer, DS_studentInfoSerializer
#Update-1.1 -> 1.2
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
#Update-1.3 -> 1.4
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
#Update-1.5
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
#LastUpdate-1.6
from rest_framework import viewsets

#-----------------------------------------------------------|Easy & shortcut way|--------------------------------------------------------------------------
#Update-1.1
@api_view(['GET', 'POST','PUT', 'PATCH', 'DELETE'])
def teacher_create(request, pk=None):
    if request.method == 'GET':
        if pk is not None:
            #Complex data
            t_data = teacherInfo.objects.get(id = pk)
            #Complex to Python dict
            python_dict = teacherInfoSerializer(t_data)
            return Response(python_dict.data)
        
        t_data = teacherInfo.objects.all()
        python_dict = teacherInfoSerializer(t_data, many=True)
        return Response(python_dict.data)
    
    if request.method == 'POST':
        teacher_info = teacherInfoSerializer(data=request.data)
        if teacher_info.is_valid():
            teacher_info.save()
            return Response({"Data inserted successfully!"})
        return Response(teacher_info.errors)
    
    if request.method == 'PUT':
        teacher_info = teacherInfo.objects.get(id = pk)
        serializer = teacherInfoSerializer(teacher_info, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg: Full data updated successfully!'})
        return Response(serializer.errors)
    
    if request.method == 'PATCH':
        teacher_info = teacherInfo.objects.get(id = pk)
        serializer = teacherInfoSerializer(teacher_info, data = request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({pk,'no id is partially updated successfully!'})
        return Response(serializer.errors)
    
    if request.method == 'DELETE':
        info = teacherInfo.objects.get(id = pk)
        info.delete()
        return Response({pk, 'data deleted successfully!'})

#-------------------------------------------------------------------|More Easy and shortcut way|--------------------------------------------------------
#Update-1.2
class createCourses(APIView):
    def get(self, request, pk=None, format = None):
        if pk is not None:
            #Complex data
            course_data = courses.objects.get(id = pk)
            #Complex to Python dict
            python_dict = courseSerializer(course_data)
            return Response(python_dict.data)
            
        course_data = courses.objects.all()
        python_dict = courseSerializer(course_data, many=True)
        return Response(python_dict.data)
        
    def post(self, request, format = None):
        course_info = courseSerializer(data=request.data)
        if course_info.is_valid():
            course_info.save()
            return Response({"Data inserted successfully!"})
        return Response(course_info.errors)
    
    def put(self, request, pk, format = None):
        course_info = courses.objects.get(id = pk)
        serializer = courseSerializer(course_info, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg: Full data updated successfully!'})
        return Response(serializer.errors)
    
    def patch(self, request, pk, format = None):
        course_info = courses.objects.get(id = pk)
        serializer = courseSerializer(course_info, data = request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({pk,'no id is partially updated successfully!'})
        return Response(serializer.errors)
    
    def delete(self, request, pk, format = None):
        info = courses.objects.get(id = pk)
        info.delete()
        return Response({pk, 'data deleted successfully!'})
    
#-------------------------------------------------------------|Most Easiest and shortcut way|---------------------------------------------------------------
#Update-1.3
"""class createStudentList(GenericAPIView, ListModelMixin):
    queryset = studentInfo_DataScience.objects.all()
    serializer_class = DS_studentInfoSerializer
    def get(self, request, *args, **kwrgs ):
        return self.list(request, *args, **kwrgs)
    
class CreateStudentModelMixin(GenericAPIView, CreateModelMixin):
    queryset =  studentInfo_DataScience.objects.all()
    serializer_class = DS_studentInfoSerializer
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
class retrieveStudentData(GenericAPIView, RetrieveModelMixin):
    queryset = studentInfo_DataScience.objects.all()
    serializer_class = DS_studentInfoSerializer
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
class updateStudentInfo(GenericAPIView, UpdateModelMixin):
    queryset = studentInfo_DataScience.objects.all()
    serializer_class = DS_studentInfoSerializer
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
class destroyStudentInfo(GenericAPIView, DestroyModelMixin):
    queryset = studentInfo_DataScience.objects.all()
    serializer_class = DS_studentInfoSerializer
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
"""
#.....................................................................................................
#CRUD opetarions => Create-Retrieve-Update-Delete
#Update-1.4
class getStudentList_createStudent(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = studentInfo_DataScience.objects.all()
    serializer_class = DS_studentInfoSerializer

    def get(self, request, *args, **kwrgs ): #Return the student list
        return self.list(request, *args, **kwrgs)
    
    def post(self, request, *args, **kwargs): #Create student
        return self.create(request, *args, **kwargs)
    
class retrieve_update_delete(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = studentInfo_DataScience.objects.all()
    serializer_class = DS_studentInfoSerializer

    def get(self, request, *args, **kwargs):  #Return specific student based on pk(primary key)
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs): #Full specific update
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs): #Delete specific student
        return self.destroy(request, *args, **kwargs)
    
#-------------------------------------------|Very Most Easiest and shortcut way(We will always follow this way|-----------------------------------------------
#Update-1.5
class listCreate_student(ListCreateAPIView):
    queryset = studentInfo_DataScience.objects.all()
    serializer_class = DS_studentInfoSerializer

class retrieveUpdateDestroy_Student(RetrieveUpdateDestroyAPIView):
    queryset = studentInfo_DataScience.objects.all()
    serializer_class = DS_studentInfoSerializer

#.................................................|Very Most Easiest and shortcut way(We will always follow this way|------------------------------------------
#LastUpdate-1.6
class listCreateRetrieveUpdateDelete_viewSets(viewsets.ModelViewSet):
    queryset = studentInfo_DataScience.objects.all()
    serializer_class = DS_studentInfoSerializer