from django.urls import path , include
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login',views.user_login,name="login"),
    path('logout',views.user_logout,name="logout"),
    path('employee',views.create_employee,name="employee"),
    path('employer',views.create_employer,name="employer"),
    path('<str:slug>',views.profile,name="profile")
]
