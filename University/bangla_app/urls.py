from django.urls import path
#For class base view
from . import views
from . views import bangla_info

urlpatterns = [
    path('', views.welcome_msg),
    path('bng/', bangla_info.as_view()),
    path('stinfo/', views.student_Info),
    path('stinfo2/<int:pk>', views.student_Instance),
    path('desrlz/', views.studentInfo_create),
]




