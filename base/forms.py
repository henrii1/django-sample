from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import User, ChatMessage, CodeMessage, CourseInformation


# class MyUserCreationFrom(UserCreationForm):
#     # Define custom error messages for password field
#     error_messages = {
#         'password_mismatch': "The two password fields didn't match.",
#         'password_too_short': "Password must be at least 8 characters long.",
#         'password_too_common': "This password is too common.",
#         # Add more custom error messages as needed
#     }

#     # Override the __init__ method to set custom error messages
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         # Set custom error messages for the password field
#         self.fields['password1'].error_messages.update({
#             'password_too_short': self.error_messages['password_too_short'],
#             'password_too_common': self.error_messages['password_too_common'],
#             # Add more custom error messages as needed
#         })

#     class Meta:
#         model = User
#         fields = ['name', 'username', 'email', 'password1', 'password2']


class MyUserCreationFrom(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password1', 'password2']



class ChatUserForm(ModelForm):
    class Meta:
        model = ChatMessage
        fields = ['user_message']


class ChatAIForm(ModelForm):
    class Meta:
        model = ChatMessage
        fields = ['ai_message']


class CodeUserForm(ModelForm):
    class Meta:
        model = CodeMessage
        fields = ['user_message']


class CodeAIForm(ModelForm):
    class Meta:
        model = CodeMessage
        fields = ['ai_message']


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['avatar', 'name', 'email', 'username', 'bio']


class CourseForm(ModelForm):
    class Meta:
        model = CourseInformation
        fields = "__all__"
    


