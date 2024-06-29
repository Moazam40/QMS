from django.db import models

# Create your models here.

class StudentInfo(models.Model):
    username = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    country = models.CharField(max_length=150)
    password = models.CharField(max_length=100)
    
         
    def __str__(self):
        return self.username
    
class ContactForm(models.Model):
    username = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    message = models.TextField()
    
    def __str__(self):
        return self.username
    
class teacherDetail(models.Model):
    name = models.CharField(max_length=150)
    playlist = models.CharField(max_length=50)
    video = models.CharField(max_length=50)
    like = models.CharField(max_length=50)
    comment = models.CharField(max_length=50)
    
    def GetAllTeacher():
        return teacherDetail.objects.all()
        
    
    def __str__(self):
        return self.name
    

    
    

