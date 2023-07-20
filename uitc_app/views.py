from django.shortcuts import render
from .models import Courses,Student,Student_work,Signup,Teacher
from .serializers import CoursesSerializer,StudentSerializer,Student_workSerializer,SignupSerializer,TeacherSerializer,\
CoursesAPISerializer,StudentAPISerializer,Student_workAPISerializer,SignupAPISerializer,TeacherAPISerializer
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.

class CoursesViewset(viewsets.ModelViewSet):
    queryset = Courses.objects.filter(status=True)
    serializer_class = CoursesSerializer
    permission_classes = [AllowAny]

class StudentViewset(viewsets.ModelViewSet):
    queryset = Student.objects.filter(status=True)
    serializer_class = StudentSerializer
    permission_classes = [AllowAny]

class Student_workViewset(viewsets.ModelViewSet):
    queryset = Student_work.objects.filter(status=True)
    serializer_class = Student_workSerializer
    permission_classes = [AllowAny]

class SignupViewset(viewsets.ModelViewSet):
    queryset = Signup.objects.filter(status=True)
    serializer_class = SignupSerializer
    permission_classes = [AllowAny]

class TeacherViewset(viewsets.ModelViewSet):
    queryset = Teacher.objects.filter(status=True)
    serializer_class = TeacherSerializer
    permission_classes = [AllowAny]


""" API """

class CoursesAPIViewset(viewsets.ModelViewSet):
    queryset = Courses.objects.filter(status=True)
    serializer_class = CoursesAPISerializer
    permission_classes = [AllowAny]
    lookup_field = 'slug'

class StudentAPIViewset(viewsets.ModelViewSet):
    queryset = Student.objects.filter(status=True)
    serializer_class = StudentAPISerializer
    permission_classes = [AllowAny]
    lookup_field = 'slug'

class Student_workAPIViewset(viewsets.ModelViewSet):
    queryset = Student_work.objects.filter(status=True)
    serializer_class = Student_workAPISerializer
    permission_classes = [AllowAny]
    lookup_field = 'slug'

class SignupAPIViewset(viewsets.ModelViewSet):
    queryset = Signup.objects.filter(status=True)
    serializer_class = SignupAPISerializer
    permission_classes = [AllowAny]
    lookup_field = 'slug'

class TeacherAPIViewset(viewsets.ModelViewSet):
    queryset = Teacher.objects.filter(status=True)
    serializer_class = TeacherAPISerializer
    permission_classes = [AllowAny]
    lookup_field = 'slug'

""" Authentification Views """
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


