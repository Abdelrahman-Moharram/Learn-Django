
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/', include("Home.api.urls", namespace="home_apis")),
    path('admin/', admin.site.urls),
]
