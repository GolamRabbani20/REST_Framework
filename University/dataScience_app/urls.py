from django.urls import path
from . import views

urlpatterns = [
    #For teacher
    path('', views.teacher_create),
    path('json2/<int:pk>', views.teacher_create),

    #For Course
    path('course/', views.createCourses.as_view()),
    path('course2/<int:pk>', views.createCourses.as_view()),
    
    #For Student
    #path('getStlist/', views.createStudentList.as_view()),
    #path('stcreate/', views.CreateStudentModelMixin.as_view()),
    path("st_getpost/", views.getStudentList_createStudent.as_view(), name="studentgetpost"),

    #path('retrieve/<int:pk>', views.retrieveStudentData.as_view()),
    #path('updateSt/<int:pk>', views.updateStudentInfo.as_view()),
    #path('deleteSt/<int:pk>', views.destroyStudentInfo.as_view()),
    path('crud/<int:pk>', views.retrieve_update_delete.as_view(), name='CRUD'),

    path('listCreate/', views.listCreate_student.as_view(), name="listCreate"),
    path('rud/<int:pk>', views.retrieveUpdateDestroy_Student.as_view(), name="RetrieveUpdateDestroy"),
]
 