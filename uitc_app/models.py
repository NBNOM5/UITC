import uuid
from django.db import models
from django.core.validators import RegexValidator

# from phone_field import PhoneField
from autoslug import AutoSlugField

_validate_phone = RegexValidator(
    regex=r"^[\+]?[9]{2}[8]?[0-9]{2}?[0-9]{3}?[0-9]{2}?[0-9]{2}$",
    message="Telefon raqamingiz 9 bilan boshlanishi va 12 belgidan oshmasligi lozim. Masalan: 998334568978",
)

STUDENT_STATUS = (
    ('now',"O'qiyapdi"),
    ('end','Tamomlagan'),
    ('working','Ishlayotgan')
)

class Courses(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nomi")
    slug = AutoSlugField(populate_from="name")

    status = models.CharField(max_length=50,  default="active", verbose_name="Holati")
    created_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('-created_at',)
        
    def str(self):
        return self.name


class Student(models.Model):
    full_name = models.CharField(max_length=200, verbose_name="Ism sharif")
    username = models.CharField(max_length=10, verbose_name="Username", unique=True,\
        error_messages={'unique':"Ushbu username mavjud!!!"})
    slug = AutoSlugField(populate_from="full_name")
    phone = models.CharField(max_length=12, validators=[_validate_phone], verbose_name="Telefon raqam")
    email = models.EmailField(verbose_name="Email", blank=True, null=True)
    photo = models.ImageField(verbose_name="Rasmi", upload_to="student_photo")
    adress = models.CharField(max_length=300, verbose_name="Manzil")
    finish = models.PositiveIntegerField(verbose_name="Imtihon foizi", default=0, blank=True, null=True)
    sertificate = models.FileField(upload_to="students_sertificates", verbose_name="Sertifikat", blank=True, null=True)
    start_date = models.DateField(verbose_name="Boshlagan vaqti")
    end_date = models.DateField(verbose_name="Tugatgan vaqti", blank=True, null=True)
    # student_status = models.CharField(max_length=10, choices=STUDENT_STATUS, default='end', verbose_name="O'quvchining holati")
    courses = models.ForeignKey(Courses, on_delete=models.CASCADE, related_name="studentcourses", verbose_name="Kurs")
    texnology = models.CharField(max_length=500, verbose_name="Texnologiyalari")
    # work_space = models.CharField(max_length=500, verbose_name="Ish joyi", blank=True, null=True)
    # work_url = models.CharField(max_length=500, verbose_name="Url manzil", blank=True, null=True)

    status = models.CharField(max_length=50,  default="active", verbose_name="Holati",blank=True,null=True)
    created_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('-created_at',)
        
    def str(self):
        return self.full_name

 
class Student_work(models.Model):
    """" O'quvchilarning ishlari haqidagi class """
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="student_work")
    name = models.CharField(max_length=250, verbose_name="Loyiha nomi")
    slug = AutoSlugField(populate_from="name")
    body = models.TextField(verbose_name="Loyiha haqida", blank=True, null=True)
    # url = models.CharField(max_length=255, verbose_name="URL manzil", blank=True, null=True)
    photo = models.ImageField(upload_to="students_work", verbose_name="Rasmi", blank=True, null=True)

    status = models.CharField(max_length=50,  default="active", verbose_name="Holati",blank=True,null=True)
    created_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('-created_at',)
        
    def str(self):
        return self.name


class Signup(models.Model):
    name = models.CharField(max_length=100, verbose_name="Ism")
    slug = AutoSlugField(populate_from="name")
    surname = models.CharField(max_length=100, verbose_name="Familya")
    phone = models.CharField(max_length=12, validators=[_validate_phone], verbose_name="Telefon raqam")
    courses = models.ForeignKey(Courses, on_delete=models.CASCADE, related_name="courses", verbose_name="Kurs")
    status = models.BooleanField(default=False, verbose_name="Holati",blank=True,null=True)
    created_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('-created_at',)
        
    def str(self):
        return self.name


class Teacher(models.Model):
    full_name = models.CharField(max_length=150)
    slug = AutoSlugField(populate_from="full_name")
    photo = models.ImageField(upload_to="teacher_photo/%Y/%m/%d/", verbose_name="Rasm")
    expertise = models.CharField(max_length=250)
    year = models.PositiveIntegerField()
    
    status = models.CharField(max_length=50, default="active", verbose_name="Holati",blank=True,null=True)
    created_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('-created_at',)
        
    def str(self):
        return self.full_name