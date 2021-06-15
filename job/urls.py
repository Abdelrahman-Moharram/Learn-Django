
from django.contrib import admin
from django.urls import path , include
from . import views

urlpatterns = [
    path('browse/', views.jobList),
    path('', views.jobList),
    path('<int:id>', views.jobDetail),

]
