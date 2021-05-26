from os import name
from django.urls import  path
from .import views

urlpatterns = [
    path('', views.admin_login, name='login'),
    path('index',views.index,name='index'),
    path('marks',views.marks,name='marks'),
    path('teacherdata',views.teacherdata,name='teacherdata'),
    path('teacherattendance',views.teacherattendance,name='teacherattendance'),
    path('studentdata',views.studentdata,name='studentdata'),
    path('Student_Attendance',views.student_Attendance,name='Student_Attendance'),
    path('studentfolder',views.studentfolder,name='studentfolder'),
    path('admin/',views.Admin,name="admin/")
]
