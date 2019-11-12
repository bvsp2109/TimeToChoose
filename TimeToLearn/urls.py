"""TimeToLearn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from onlineapp import views

urlpatterns = [

    url(r'^admin/', admin.site.urls),

#student institute registrations forms

    url(r'student/register/',views.Student_Register),
    url(r'institute/register/',views.Institute_Register),
    url('accounts/', include('django.contrib.auth.urls')),
    url(r'accounts/login/',views.Login),
    url(r'logout/', views.LogOut),


#student details urls

    url(r'index/', views.Student_Home_view),
    # url(r'studata/', views.Student_Details),
    url(r'demoregister/', views.Demo_Studets),
    url(r'demostudentsdata/', views.Demo_Studets_Data),

#institute details urls

    url(r'intstitute/register/', views.Institute_Register),
    # url(r'institute/details/', views.InstituteDetails),
    url(r'intupload/', views.Institute_Upload_Course_Data),
    url(r'intupcomingdemo/', views.Upcoming_Demo),
    url(r'welcome/',views.Institute_Home_view),
    url(r'instituteprofile/',views.Profile),

#home page navigation related details

    url(r'home/', views.Register_Navigation),
    url(r'logindetails/',views.Home),


]
