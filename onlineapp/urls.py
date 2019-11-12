from django.contrib import admin
from django.urls import path,include
from  onlineapp import views



urlpatterns = [
    path('admin/', admin.site.urls),

    path('home/', views.Home_view),
    path('studata/',views.Student_Details),
    path('logout/', views.LogOut),
    path('intstitute/register/', views.Institute_Register),
    # path('accounts/institutelogin/',views.login_view),
    # path('redirection/', views.Register_Navigation),
    path('institute/details/', views.InstituteDetails),
    path('intupload/', views.Institute_Upload_Course_Data),
    path('intupcomingdemo/', views.Upcoming_Demo),
    path('demoregister/', views.Demo_Studets),
    path('demostudentsdata/', views.Demo_Studets_Data),

]