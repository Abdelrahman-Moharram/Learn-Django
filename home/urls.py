
from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path("", views.index, name='index'),
		path("delete/<str:id>", views.delete, name="delete")
]
