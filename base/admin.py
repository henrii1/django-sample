from django.contrib import admin

from .models import User, ChatMessage, CodeMessage, CourseInformation
# Register your models here.

admin.site.register(User)
admin.site.register(ChatMessage)
admin.site.register(CodeMessage)
admin.site.register(CourseInformation)


