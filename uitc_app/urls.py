from django.urls import path, include
from rest_framework import routers
from .views import CoursesViewset, StudentViewset, Student_workViewset,SignupViewset,TeacherViewset,\
CoursesAPIViewset, StudentAPIViewset, Student_workAPIViewset,SignupAPIViewset,TeacherAPIViewset

router = routers.DefaultRouter()
router.register(r'courses', CoursesViewset)
router.register(r'student', StudentViewset)
router.register(r'student-work', Student_workViewset)
router.register(r'signup', SignupViewset)
router.register(r'teacher', TeacherViewset)

router.register(r'courses-api', CoursesAPIViewset)
router.register(r"student-api", StudentAPIViewset)
router.register(r"student_work-api", Student_workAPIViewset)
router.register(r"signup-api", SignupAPIViewset)
router.register(r"teacher-api", TeacherAPIViewset)

urlpatterns = [
    path('', include(router.urls)),
    
    
]