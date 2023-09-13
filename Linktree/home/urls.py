from django.contrib import admin
from django.urls import path 
from home import views

urlpatterns = [
    path('',views.index,name='home'),
    path('login',views.loginUser,name="loginuser"),
    path('signup',views.signup,name="signup"),
    path('developerprofile',views.developerprofile,name="developerprofile"),
    path('logoutuser',views.logoutuser,name="logoutuser"),
    path("update",views.update,name="update"),
    path("home",views.home,name="home"),
    path("create",views.create,name="create")
]