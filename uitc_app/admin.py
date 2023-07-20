from django.contrib import admin
from .models import Courses,Student,Student_work,Signup,Teacher

# Register your models here.

@admin.register(Courses)
class CoursesAdmin(admin.ModelAdmin):
    list_display = ('name','id','slug' , 'status', 'created_at')
    list_filter = ('status', 'created_at')
    list_editable = ('status',)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name','username','slug','phone','email','photo','adress','finish',\
                'sertificate','start_date','end_date','courses','texnology','status', 'created_at')
    list_filter = ('phone','email','status', 'created_at')
    list_editable = ('status',)

@admin.register(Student_work)
class Student_workAdmin(admin.ModelAdmin):
    list_display = ('id', 'student','name','slug','body','photo','status', 'created_at')
    list_filter = ('status', 'created_at')
    list_editable = ('status',)

@admin.register(Signup)
class SignupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','slug','surname','phone','courses','status', 'created_at')
    list_filter = ('status', 'created_at')
    list_editable = ('status',)

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name','slug','photo','expertise','year','status', 'created_at')
    list_filter = ( 'status', 'created_at')
    list_editable = ('status',)











