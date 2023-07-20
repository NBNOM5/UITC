from .models import Courses,Student,Student_work,Signup,Teacher
from rest_framework import serializers

""" CRUD API"""
class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = ('__all__')

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('__all__')

class Student_workSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student_work
        fields = ('__all__')

class SignupSerializer(serializers.ModelSerializer):   
    class Meta:
        model = Signup
        fields = ('__all__')

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('__all__')

""" API """
class CoursesAPISerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = ('id', 'name','slug')

class StudentAPISerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'full_name','username','slug','phone','email','photo','adress','finish','sertificate',\
                  'start_date','end_date','courses','texnology')

class Student_workAPISerializer(serializers.ModelSerializer):
    class Meta:
        model = Student_work
        fields = ('id', 'student','name','slug','body','photo')

class SignupAPISerializer(serializers.ModelSerializer):   
    class Meta:
        model = Signup
        fields = ('id', 'name','slug','surname','phone','courses')

class TeacherAPISerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('id', 'full_name','slug','photo','expertise','year')







    








