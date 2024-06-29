from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def home(request):
    if request.user.is_anonymous:
        return redirect('/login')
    else:
        
        return render(request, 'home.html')
        
    
def about(request):
    if request.user.is_anonymous:
        return redirect('/login')
    else:
        return render(request, 'about.html')

def contact(request):
    if request.user.is_anonymous:
        return redirect('/login')
    else:
        if request.method == 'POST':
            username = request.POST['name']
            email = request.POST['email']
            phone = request.POST['phone']
            message = request.POST['msg']
            user_contact = ContactForm.objects.create(username=username,email=email,phone=phone,message=message)
            user_contact.save()
        
        return render(request, 'contact.html')

def courses(request):
    if request.user.is_anonymous:
        return redirect('/login')
    else:
        videoid = 'AJ7qQBsrghI'
        return render(request, 'courses.html', {'videoid' : videoid})

def loginView(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        print(f'{username,password}')
        user = authenticate(username=username, password=password)
        if user is not None:
            print('Hello')
            login(request, user)
            messages.warning(request, "You're successfully Login in.")
            return redirect('/') 
        else:
            print('No')
            return render(request, 'login.html')  
    return render(request, 'login.html')

def playlist(request):
    if request.user.is_anonymous:
        return redirect('/login')
    else:
        return render(request, 'playlist.html')

def profile(request):
    if request.user.is_anonymous:
        return redirect('/login')
    else:
        return render(request, 'profile.html')
    

def register(request):
    if request.method == 'POST':
        username = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        country = request.POST['country']
        password = request.POST['pass']
        c_password = request.POST['c_pass']
        if password == c_password:
            user = User.objects.create(username=username,email=email)
            user_info = StudentInfo.objects.create(username=username,email=email,phone=phone,country=country)
            user.set_password(password)
            user.save()
            messages.warning(request, "You're successfully Sign in.")
            return redirect('/login')
        else:
            messages.warning(request, "Your password and confirm password is not same!")
            return redirect('/register')
    return render(request, 'register.html')

def teacher_profile(request):
    if request.user.is_anonymous:
        return redirect('/login')
    else:
        return render(request, 'teacher_profile.html')
    

def teachers(request):
    if request.user.is_anonymous:
        return redirect('/login')
    else:
        teachers = teacherDetail.objects.all()
        data = {
            'teachers' : teachers
        }
        return render(request, 'teachers.html', data)
    

def update(request):
    if request.user.is_anonymous:
        return redirect('/login')
    else:
        return render(request, 'update.html')
    

def watch_video(request):
    if request.user.is_anonymous:
        return redirect('/login')
    else:
        return render(request, 'watch-video.html')
    

