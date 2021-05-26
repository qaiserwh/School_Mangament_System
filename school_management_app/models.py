
from django.contrib.admin.filters import SimpleListFilter
from django.db import models
from django.db.models.deletion import PROTECT


#Teacher section

class Teacher(models.Model):
    name =models.CharField(max_length=550)
    age =models.IntegerField()
    photo =models.ImageField(upload_to='photos',null=True,blank=True)
    salary =models.CharField(max_length=50)
    phonenumber=models.CharField(max_length=50,null=True)
    Email=models.EmailField(null=True,blank=True)
    address=models.CharField(max_length=50)
    Departments=models.CharField(max_length=50)
    Degree =models.CharField(max_length=50)
    
    def __str__(self):
        return self.name



        
class Teacher_Attendance(models.Model):
    status_Teacher=[
        ('موجود','موجود'),
        ('غائب','غائب'),
        ('في اجازة','في اجازة')
    ]
    name_Teacher=models.ForeignKey(Teacher, on_delete=models.PROTECT)
    status =models.CharField(max_length=50,choices=status_Teacher)
    date=models.DateField()

    def __str__(Self):
        return Self.status

#Student section
class Stage(models.Model):
    stage_name=models.CharField(max_length=100)
    def __str__(Self):
        return Self.stage_name
    
class Student(models.Model):
    name =models.CharField(max_length=250)
    age =models.IntegerField()
    photo =models.ImageField(upload_to='photos')
    parents_phonenumber=models.CharField(max_length=50,null=True)
    parents_Email=models.EmailField(null=True,blank=True)
    address=models.CharField(max_length=200)
    stage_name=models.ForeignKey(Stage,on_delete=models.PROTECT)

    
    def __str__(self):
        return self.name




        
class Student_Attendance(models.Model):
    status_Student=[
        ('موجود','موجود'),
        ('غائب','غائب'),
        ('في اجازة','في اجازة')
    ]
    name_Student=models.ForeignKey(Student, on_delete=models.PROTECT)
    class_name=models.ForeignKey(Stage, on_delete=models.PROTECT)
    status =models.CharField(max_length=50,choices=status_Student)
    date=models.DateField()

    def __str__(Self):
        return Self.status
class Marks_semester(models.Model):
    status_Student=[
        ('ناجح','ناجح'),
        ('مكمل','مكمل'),
        ('راسب','راسب'),
    ]
    
    student_name = models.ForeignKey(Student , on_delete=models.PROTECT)
    class_name = models.ForeignKey(Stage , on_delete=models.PROTECT)
    Subject_name1 = models.CharField(max_length=50,null=True,blank=True)
    Subject_mark1 =models.CharField(max_length=50,null=True,blank=True)
    Subject_name2 = models.CharField(max_length=50,null=True,blank=True)
    Subject_mark2 =models.CharField(max_length=50,null=True,blank=True)
    Subject_name3 = models.CharField(max_length=50,null=True,blank=True)
    Subject_mark3=models.CharField(max_length=50,null=True,blank=True)
    Subject_name4 = models.CharField(max_length=50,null=True,blank=True)
    Subject_mark4 =models.CharField(max_length=50,null=True,blank=True)
    Subject_name5 = models.CharField(max_length=50,null=True,blank=True)
    Subject_mark5 =models.CharField(max_length=50,null=True,blank=True)
    Subject_name6 = models.CharField(max_length=50,null=True,blank=True)
    Subject_mark6 =models.CharField(max_length=50,null=True,blank=True)
    Subject_name7 = models.CharField(max_length=50,null=True,blank=True)
    Subject_mark7 =models.CharField(max_length=50,null=True,blank=True)
    status = models.CharField(max_length=50,choices=status_Student)
    #marks of second half
    Subject_name8 = models.CharField(max_length=50,null=True,blank=True)
    Subject_mark8 =models.CharField(max_length=50,null=True,blank=True)
    Subject_name9 = models.CharField(max_length=50,null=True,blank=True)
    Subject_mark9 =models.CharField(max_length=50,null=True,blank=True)
    Subject_name10 = models.CharField(max_length=50,null=True,blank=True)
    Subject_mark10 =models.CharField(max_length=50,null=True,blank=True)
    Subject_name11 = models.CharField(max_length=50,null=True,blank=True)
    Subject_mark11 =models.CharField(max_length=50,null=True,blank=True)
    Subject_name12 = models.CharField(max_length=50,null=True,blank=True)
    Subject_mark12 =models.CharField(max_length=50,null=True,blank=True)
    Subject_name13 = models.CharField(max_length=50,null=True,blank=True)
    Subject_mark13 =models.CharField(max_length=50,null=True,blank=True)
    Subject_name14 = models.CharField(max_length=50,null=True,blank=True)
    Subject_mark14 =models.CharField(max_length=50,null=True,blank=True)
    status2 = models.CharField(max_length=50,choices=status_Student)
    
    def __str__(Self):
        return Self.status
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
