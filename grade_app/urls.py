from django.contrib import admin
from django.urls import path, include
from grade_app import views as grade_app_views

urlpatterns =[
    path('dashboard',grade_app_views.dashboard,name='dashboard'),
    path('form',grade_app_views.form,name='form'),
    path('',grade_app_views.form,name='home')
]
