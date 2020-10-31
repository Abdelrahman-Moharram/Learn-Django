from django.contrib import admin
from django.urls import path , include
from . import views

app_name = 'job'

urlpatterns = [
    path('',views.jobs,name="home"),
    path('add',views.addJob,name="add"),
    path('<str:slug>',views.job_details,name="detail")
]
