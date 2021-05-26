from school_management_app.models import Marks_semester, Stage, Student, Student_Attendance,  Teacher, Teacher_Attendance
from django.contrib import admin

# Register your models here.
class TeacherAdmin(admin.ModelAdmin):
    list_display=['name','age','salary','phonenumber','Email','address','Departments','Degree']
    search_fields=['name']
class StudentAdmin(admin.ModelAdmin):
    list_display=['name','age','parents_phonenumber','parents_Email','address','stage_name']
    search_fields=['name']
class Teacher_AttendanceAdmin(admin.ModelAdmin):
    list_display=['name_Teacher','status','date',]
    search_fields=['name_Teacher']
class Student_AttendanceAdmin(admin.ModelAdmin):
    list_display=['name_Student','class_name','status','date',]
    search_fields=['name_Student']
#class MarksAdmin(admin.ModelAdmin):
    #list_display=['student_name','class_name','status','status2']
    #search_fields=['student_name']
admin.site.register(Teacher ,TeacherAdmin)
admin.site.register(Stage)
admin.site.register(Teacher_Attendance,Teacher_AttendanceAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Student_Attendance,Student_AttendanceAdmin)
admin.site.register(Marks_semester)


