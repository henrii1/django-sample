from django.contrib.auth.models import AbstractUser, Group, Permission
from django.contrib.sessions.models import Session
from django.db import models


# Create your models here.

class User(AbstractUser):
    #pass  # when creating a superuser

    name = models.CharField(max_length=300, null=True)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True)
    avatar =models.ImageField(null=True, default='avatar.svg')
    USERNAME_FIELD= 'email'
    REQUIRED_FIELDS= []


class ChatMessage(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    session_id = models.ForeignKey(Session, on_delete=models.CASCADE)
    user_message = models.TextField(null=True)
    ai_message = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']
    
    def __str__(self):
        return f'Chat Session ID:({self.session_id})'
    
class CodeMessage(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    session_id = models.ForeignKey(Session, on_delete=models.CASCADE)
    user_message = models.TextField(null=True)
    ai_message = models.TextField(null=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f'Code Session ID:({self.session_id})'
    

class CourseInformation(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    session_id = models.ForeignKey(Session, on_delete=models.CASCADE)
    course_name = models.CharField(max_length=1000)
    course_definition = models.TextField()
    course_description = models.TextField()
    learning_objectives = models.TextField()
    timeline = models.CharField(max_length=1000, null=True)
    recommended_experience = models.CharField(max_length=1000, null=True)
    tools_needed = models.TextField(null=True)
    course_content = models.TextField()

    def __str__(self):
        return str(self.course_name)
    
    

    


    




