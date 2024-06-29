from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('courses/', views.courses, name='courses'),
    path('login/', views.loginView, name='login'),
    path('playlist/', views.playlist, name='playlist'),
    path('profile/', views.profile, name='profile'),
    path('register/', views.register, name='register'),
    path('teacher-profile/', views.teacher_profile, name='teacher-profile'),
    path('teacher/', views.teachers, name='teachers'),
    path('update/', views.update, name='update'),
    path('watch-video/', views.watch_video, name='watch-video'),
    
]