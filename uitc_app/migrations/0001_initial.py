# Generated by Django 4.2 on 2023-07-19 07:56

import autoslug.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nomi')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name')),
                ('status', models.CharField(default='active', max_length=50, verbose_name='Holati')),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200, verbose_name='Ism sharif')),
                ('username', models.CharField(error_messages={'unique': 'Ushbu username mavjud!!!'}, max_length=10, unique=True, verbose_name='Username')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='full_name')),
                ('phone', models.CharField(max_length=12, validators=[django.core.validators.RegexValidator(message='Telefon raqamingiz 9 bilan boshlanishi va 12 belgidan oshmasligi lozim. Masalan: 998334568978', regex='^[\\+]?[9]{2}[8]?[0-9]{2}?[0-9]{3}?[0-9]{2}?[0-9]{2}$')], verbose_name='Telefon raqam')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email')),
                ('photo', models.ImageField(upload_to='student_photo', verbose_name='Rasmi')),
                ('adress', models.CharField(max_length=300, verbose_name='Manzil')),
                ('finish', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Imtihon foizi')),
                ('sertificate', models.FileField(blank=True, null=True, upload_to='students_sertificates', verbose_name='Sertifikat')),
                ('start_date', models.DateField(verbose_name='Boshlagan vaqti')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='Tugatgan vaqti')),
                ('texnology', models.CharField(max_length=500, verbose_name='Texnologiyalari')),
                ('status', models.CharField(blank=True, default='active', max_length=50, null=True, verbose_name='Holati')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('courses', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='studentcourses', to='uitc_app.courses', verbose_name='Kurs')),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=150)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='full_name')),
                ('photo', models.ImageField(upload_to='teacher_photo/%Y/%m/%d/', verbose_name='Rasm')),
                ('expertise', models.CharField(max_length=250)),
                ('year', models.PositiveIntegerField()),
                ('status', models.CharField(blank=True, default='active', max_length=50, null=True, verbose_name='Holati')),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='Student_work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Loyiha nomi')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name')),
                ('body', models.TextField(blank=True, null=True, verbose_name='Loyiha haqida')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='students_work', verbose_name='Rasmi')),
                ('status', models.CharField(blank=True, default='active', max_length=50, null=True, verbose_name='Holati')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_work', to='uitc_app.student')),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='Signup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Ism')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name')),
                ('surname', models.CharField(max_length=100, verbose_name='Familya')),
                ('phone', models.CharField(max_length=12, validators=[django.core.validators.RegexValidator(message='Telefon raqamingiz 9 bilan boshlanishi va 12 belgidan oshmasligi lozim. Masalan: 998334568978', regex='^[\\+]?[9]{2}[8]?[0-9]{2}?[0-9]{3}?[0-9]{2}?[0-9]{2}$')], verbose_name='Telefon raqam')),
                ('status', models.BooleanField(blank=True, default=False, null=True, verbose_name='Holati')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('courses', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='uitc_app.courses', verbose_name='Kurs')),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
    ]
