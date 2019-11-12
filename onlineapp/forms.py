from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import *

class InstituteSignUpForm(UserCreationForm):
    first_name = forms.CharField(label='Full Name:', widget=forms.TextInput(attrs={}))

    class Meta(UserCreationForm.Meta):
        model = User
        fields = [
            'username',
            'first_name',
            'email',
            'password1',
            'password2',
        ]

    def save(self, commit=True):
        user = super(InstituteSignUpForm,self).save(commit=False)
        user.is_teacher = True
        if commit:
            user.save()
        return user


class StudentSignUpForm(UserCreationForm):
    first_name = forms.CharField(label='Full Name:', widget=forms.TextInput(attrs={}))

    class Meta(UserCreationForm.Meta):
        model = User
        fields = [
            'username',
            'first_name',
            'email',
            'password1',
            'password2',
        ]

    def save(self, commit=True):
        user = super(StudentSignUpForm,self).save(commit=False)
        user.is_student= True
        if commit:
            user.save()
        return user



"""Profile Details """

class ProfileForm(forms.ModelForm):

    Mobile = forms.CharField(label='Mobile Number:', max_length=13,
                             widget=forms.TextInput(attrs={}))
    Address = forms.CharField(label='Current Address:',
                              widget=forms.TextInput(attrs={}))


    class Meta:
        model = Profile
        fields = ['Mobile', 'Address',]


class CourseForm(forms.ModelForm):
    Institute_Name = forms.CharField(label='Institute Name:', widget=forms.TextInput(attrs={'placeholder': 'NIIT'}))
    Faculty_Name = forms.CharField(label='Faculty Name:', widget=forms.TextInput(attrs={'placeholder': 'Pratap Billu'}))
    New_Batche = forms.DateField(label='New Batches:', widget=forms.TextInput(attrs={'placeholder': 'YYYY-MM-DD'}))
    Duration = forms.CharField(label='Duration:', widget=forms.TextInput(attrs={'placeholder': '45 days'}))
    Class_Timings = forms.TimeField(label='Class Timings:', widget=forms.TimeInput(attrs={'placeholder': '14:00:00'}))
    Free_Demo_Video = forms.URLField(label='Demo Video Urls:',
                                     widget=forms.TextInput(attrs={'placeholder': 'https://www.google.com/'}))

    class Meta:
        model = Course
        fields = ['Institute_Name', 'Faculty_Name', 'New_Batche', 'Duration', 'Class_Timings', 'Free_Demo_Video']


class DemoStudentDetails(forms.ModelForm):
    First_Name = forms.CharField(label='First Name',widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    Last_Name = forms.CharField(label='Last Name',widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    Email = forms.EmailField(label='Email',widget=forms.TextInput(attrs={'placeholder': 'test@gmail.com'}))
    Mobile_Number = forms.CharField(label='Mobile',widget=forms.TextInput(attrs={'placeholder': 'Mobile Number'}))
    Course = forms.CharField(label='Course Name',widget=forms.TextInput(attrs={'placeholder': 'Python or java'}))
    Location = forms.CharField(label='Current Location',widget=forms.TextInput(attrs={'placeholder': 'Current Location'}))

    class Meta:
        model = DemoStudents
        fields = ['First_Name','Last_Name','Email','Mobile_Number','Course','Location']
