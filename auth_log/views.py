from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from accounts.models import MyUser
from django.contrib.auth.hashers import check_password
# Create your views here.

from django.http import HttpResponse


def index(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email,password,444444444)
        user_exists = MyUser.objects.filter(email=email).first()
        print(user_exists,5555555555555)
        if user_exists:
            if check_password(password, user_exists.password):
                print(66666666666666)
                if request.user.is_superuser:
                    return redirect('dashboard')
            else:
                return redirect('register')
    return render(request, 'login.html')


from django.shortcuts import render, redirect
from django.contrib import messages
from accounts.models import MyUser

def register(request):
    if request.method == 'POST':
        name = request.POST.get('register_name')
        email = request.POST.get('register_email')
        password = request.POST.get('register_password')
        password1 = request.POST.get('register_password1')

        if not name or not email or not password or not password1:
            messages.error(request, 'All fields are required!')
            return redirect('register')

        if password != password1:
            messages.error(request, 'Passwords do not match!')
            return redirect('register')

        try:
            user = MyUser.objects.create_user(username=email[:30], email=email, password=password)
            user.save()
            messages.success(request, 'User registered successfully!')
            return redirect('login')
        except Exception as e:
            messages.error(request, f'Error: {str(e)}')
            return redirect('register')
    
    return render(request, 'register.html')


def dashboard(request):
    if request.method == 'GET':
        from att.models.student import Student,Course,Instructor,Attendance
        students = Student.objects.all().values_list('username','email','mobile','roll_number','department')
        print(students,333333333333333)
    return render(request, 'dashboard.html')