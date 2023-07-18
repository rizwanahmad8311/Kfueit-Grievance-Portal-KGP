# Generated by Django 4.2 on 2023-05-17 05:34

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarouselImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='carousel/images')),
            ],
        ),
        migrations.CreateModel(
            name='ComplaintCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='department/images')),
            ],
        ),
        migrations.CreateModel(
            name='FacultySignUp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=250)),
                ('lname', models.CharField(max_length=250)),
                ('user_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='HODSignUp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=250)),
                ('lname', models.CharField(max_length=250)),
                ('user_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=500)),
                ('department_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hodapp.department')),
            ],
        ),
        migrations.CreateModel(
            name='SignUp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=250)),
                ('lname', models.CharField(max_length=250)),
                ('user_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=500)),
                ('otp', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complaint_id', models.CharField(max_length=200)),
                ('resolution_status', models.BooleanField(default=False)),
                ('satisfaction_status', models.BooleanField(default=False)),
                ('feedback', models.CharField(max_length=200)),
                ('stars', models.IntegerField()),
                ('created_at', models.DateTimeField(default=datetime.datetime.today)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hodapp.signup')),
            ],
        ),
        migrations.CreateModel(
            name='LoginActivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='signup', to='hodapp.signup')),
            ],
        ),
        migrations.CreateModel(
            name='HODSignUpEmail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False)),
                ('hod_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hodapp.hodsignup')),
            ],
        ),
        migrations.CreateModel(
            name='FacultySignUpEmail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False)),
                ('faculty_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hodapp.facultysignup')),
            ],
        ),
        migrations.AddField(
            model_name='facultysignup',
            name='hod_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hodapp.hodsignup'),
        ),
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complaint_id', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('details', models.CharField(max_length=250)),
                ('hide_identity', models.BooleanField(default=False)),
                ('image', models.ImageField(blank=True, null=True, upload_to='complaint/images')),
                ('video', models.FileField(blank=True, null=True, upload_to='complaint/videos')),
                ('created_at', models.DateTimeField(default=datetime.datetime.today)),
                ('declaration', models.BooleanField(default=False)),
                ('forwarded_at', models.DateTimeField(default=datetime.datetime.today)),
                ('closed_at', models.DateTimeField(default=datetime.datetime.today)),
                ('cancel_at', models.DateTimeField(default=datetime.datetime.today)),
                ('withdrawn_at', models.DateTimeField(default=datetime.datetime.today)),
                ('is_pending', models.BooleanField(default=True)),
                ('is_forwarded', models.BooleanField(default=False)),
                ('is_canceled', models.BooleanField(default=False)),
                ('is_withdrawn', models.BooleanField(default=False)),
                ('is_completed', models.BooleanField(default=False)),
                ('is_completed_resolved', models.BooleanField(default=False)),
                ('forwarded_msg', models.CharField(blank=True, max_length=500, null=True)),
                ('canceled_msg', models.CharField(blank=True, max_length=500, null=True)),
                ('additional_info_msg', models.CharField(blank=True, max_length=500, null=True)),
                ('completed_msg', models.CharField(blank=True, max_length=500, null=True)),
                ('is_reviewed', models.BooleanField(default=False)),
                ('complaint_category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hodapp.complaintcategory')),
                ('department_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hodapp.department')),
                ('faculty_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hodapp.facultysignup')),
                ('hod_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hodapp.hodsignup')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hodapp.signup')),
            ],
        ),
    ]
