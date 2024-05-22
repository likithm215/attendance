from django.contrib import admin

# Register your models here.
from att.models.student import Student,Course,Attendance,Instructor
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Attendance)
admin.site.register(Instructor)