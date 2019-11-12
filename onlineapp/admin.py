# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *



# Register your models here.
class UserDetails(admin.ModelAdmin):
    list_display = ['id','username', 'first_name', 'email']
    search_fields = ['username', 'first_name', 'last_name', 'email']

admin.site.register(User, UserDetails)


class StudentDetailsAdmin(admin.ModelAdmin):
    list_display = ['Mobile', 'Address']
    search_fields = ()
admin.site.register(Profile, StudentDetailsAdmin)


class CourseAdmin(admin.ModelAdmin):
    list_display = ['Institute_Name', 'Faculty_Name', 'New_Batche', 'Duration', 'Class_Timings', 'Free_Demo_Video']
    search_fields = ('Institute_Name', 'Faculty_Name')


admin.site.register(Course, CourseAdmin)

admin.site.register(DemoStudents)
