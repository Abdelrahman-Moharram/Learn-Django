
from django.contrib import admin
from django.urls import path , include
from . import views

app_name = 'job'
urlpatterns = [
    path('', views.jobList,name="jobList"),
    path('browse/', views.jobList),
    path('add/', views.add_job,name="addJob"),
    path('<str:slug>', views.jobDetail,name="jobDetail"),
]
