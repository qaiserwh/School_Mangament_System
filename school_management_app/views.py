
from os import name
from.models import *
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from . forms import AdminLoginForm



# Create your views here

def marks(request):
    context={
        'marks':Marks_semester.objects.all()
    }
    
    return render(request,'content/marks.html',context)
    
def admin_login(request):
     forms = AdminLoginForm()
     if request.method == 'POST':
         forms = AdminLoginForm(request.POST)
         if forms.is_valid():
             username = forms.cleaned_data['username']
             password = forms.cleaned_data['password']
             user = authenticate(username=username, password=password)
             if user:
                 login(request,user)
                 return redirect('index')
     context = {'forms': forms}
     return render(request,'content/login.html', context)
 
def index(request):
    return render(request,'content/index.html')
def studentdata(request):
    search=Student.objects.all()
    status= None
    if 'search_name'  in request.GET:
        status =request.GET['search_name']
        if status:
            search = search.filter(status__icontains=name)
    context ={
    'student_data':search
    }
    return render(request,'content/student_data.html',context)
def teacherdata(request):
    search=Teacher.objects.all()
    status= None
    if 'search_name'  in request.GET:
        status =request.GET['search_name']
        if status:
            search = search.filter(status__icontains=name)
    context ={
    'teacher_data':search
    }
    return render(request,'content/teacher_data.html',context)

def teacherattendance(request):
    search=Teacher_Attendance.objects.all()
    status= None
    if 'search_name'  in request.GET:
        status =request.GET['search_name']
        if status:
            search = search.filter(status__icontains=name)
    context ={
    'Teacher_Attendance':search
    }
    return render(request,'content/Teacher_Attendance.html',context)
def studentfolder(request):
    context={
        'student_card':Student.objects.all()
    }
    return render(request,'content/student_folder.html',context)
def student_Attendance(request):
    search=Student_Attendance.objects.all()
    status= None
    if 'search_name'  in request.GET:
        status =request.GET['search_name']
        if status:
            search = search.filter(status__icontains=name)
    context ={
    'Student_Attendance':search
    }
    return render(request,'content/Student_Attendance.html',context)

def Admin(request):
    return render