from django.urls import path
from .views import index, MyTokenObtainPairView

from rest_framework_simplejwt.views import (
    TokenObtainPairView, # without custom claims
    TokenRefreshView,
)



app_name = "home_apis"

urlpatterns = [
    path("",index , name="index"),
    path('token', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
]
