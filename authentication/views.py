from django.contrib.auth import get_user_model

from rest_framework import viewsets, status
from rest_framework.response import Response

from .serialiazers import *

# Create your views here.
class CreateUserView(viewsets.ViewSet):
    serializer_class = UserSerializer
    
    def create(self, request):
        try:
            data = request.data
            user = get_user_model().objects.create_user(**data)

            return Response({'message':f'user created {user}'}, status=status.HTTP_201_CREATED)
        
        except Exception as err:
            return Response({'message':'error at creating user'}, status=status.HTTP_400_BAD_REQUEST)