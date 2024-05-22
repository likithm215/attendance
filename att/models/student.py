from django.contrib.auth.models import AbstractUser
from django.db import models
from accounts.models.my_user import MyUser

class Student(MyUser):
    roll_number = models.CharField(max_length=20, unique=True)
    department = models.CharField(max_length=100)
    class Meta:
        verbose_name = "Student"

class Instructor(MyUser):
    department = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Instructor"

class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.BooleanField()  # True for present, False for absent
