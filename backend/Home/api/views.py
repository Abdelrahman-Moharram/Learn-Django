from django.http import JsonResponse
from rest_framework import response, status
from rest_framework.decorators import api_view

from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import MyTokenObtainPairSerializer


@api_view(['GET'])
def index(request):
    routes = [
        '/api/token',
        '/api/token/refresh'
    ]
    return response.Response(routes, status.HTTP_200_OK)




    
class MyTokenObtainPairView(TokenObtainPairView):
    serilizer_class = MyTokenObtainPairSerializer
