from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerUser, name='register'),
    path('update-user/', views.UpdateUser, name='update-user'),
    path("change-password/", views.changePassword, name='change-password'),
    path("delete-user/", views.deleteUser, name='delete-user'),
    path('profile/', views.userProfile, name='profile'),
    path('settings/', views.settings, name='settings'),
    

]