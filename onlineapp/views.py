from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .decorators import student_required, teacher_required


def Home(request):
    if request.user.is_authenticated:
        if request.user.is_teacher:
            return redirect('/welcome/')
        else:
            return redirect('/index/')
    return render(request,'myapp/home.html')




# STUDENTS DetailS


def Student_Home_view(request):
    return render(request, 'myapp/studenthome.html')

# future demo class table creations
def Upcoming_Demo(request):
    CourseDetails = Course.objects.all()
    return render(request, 'myapp/class.html', {'CourseDetails': CourseDetails})

""" Demo registration details """

def Demo_Studets(requrest):
    form = DemoStudentDetails(requrest.POST or None, requrest.FILES or None)
    if form.is_valid():
        Instance = form.save()
        Instance.save()
        return redirect('/intupcomingdemo/')
    context = {'form': form}
    return render(requrest, 'Institute/myapp/demostudentdetails.html', context)





# INSTITUTE DETAILS


def Institute_Home_view(request):

    return render(request, 'Institute/homepage.html')



# future demo class uploading Data
def Institute_Upload_Course_Data(requrest):
    form = CourseForm(requrest.POST or None, requrest.FILES or None)
    if form.is_valid():
        Instance = form.save()
        Instance.save()
        return redirect('/welcome/')
    else:
        form = CourseForm()
    return render(requrest, 'myapp/Institute_uploded.html', {'form': form})


#demo students data fornt view

def Demo_Studets_Data(request):
    CourseDetails = DemoStudents.objects.all()
    return render(request, 'Institute/myapp/studentdata.html', {'CourseDetails': CourseDetails})





# REGISTRATIONS

"""STUDENT REGISTRATIONS"""


def Student_Register(request, *args, **kwargs):
    form = StudentSignUpForm(request.POST or None)
    profile = ProfileForm(request.POST or None)
    if form.is_valid() and profile.is_valid():
        user = form.save()
        user.save()
        userprofile = profile.save(commit=False)
        userprofile.user = user
        userprofile.save()

        return redirect('/accounts/login/')
    context = {
        'form': form, 'profile' : profile
    }
    return render(request, "registration/registration.html", context)


"""INSTITUTE REGISTRATIONS"""


def Institute_Register(request, *args, **kwargs):
    form = InstituteSignUpForm(request.POST or None)
    profile = ProfileForm(request.POST or None)
    if form.is_valid() and profile.is_valid():
        user = form.save()
        user.save()
        userprofile = profile.save(commit=False)
        userprofile.user = user
        userprofile.save()
        return redirect('/accounts/login/')
    context = {
        'form': form,'profile': profile
    }
    return render(request, "registration/registration.html", context)

def Profile(request):

    return render(request,'Institute/profile.html')

@login_required
@student_required
@teacher_required
def Login(request):
    return request(request, "registration/login.html")


def LogOut(request):
    return render(request, 'registration/logout.html')





def Register_Navigation(request):
    return render(request, 'myapp/registrationdirection.html')
