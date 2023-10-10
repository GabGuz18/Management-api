from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.models import BaseUserManager
from django.core.exceptions import ObjectDoesNotExist

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action

from .serializers import *
from .models import *
from .errorHandlers import *


# Create your views here.
class UserViewSet(viewsets.ViewSet):
    serializer_class = UserSerializer

    def create(self, request):
        try:
            data = request.data
            name = data['name']
            email = data['email']
            password = data['password']
            
            if User.objects.filter(email=email).exists():
                raise UserExistError('User already taken')
            
            user = User(
                username=BaseUserManager.normalize_email(email),
                name=name,
                email=BaseUserManager.normalize_email(email)
            )
            user.set_password(password)
            user.save()

            return Response(
                {'error':'false', 'message':f'User created: {email}'},
                status=status.HTTP_201_CREATED
            )
        except Exception as err:
            print(err)
            return Response(
                {'error':'true', 'message':f'Error: {err}'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
    @action(detail=False,methods=["post"])
    def login(self, request):
        try:
            data = request.data
            email = data["email"]
            password = data["password"]

            account = User.objects.get(email=email)

            if account:
                #user = authenticate(username=email, password=password)
                token, created = Token.objects.get_or_create(user=account)
                return Response(
                    {'error':'false', 'message':'Token created', 'token': token.key, 'user': created}, 
                    status=status.HTTP_200_OK
                )

        except ObjectDoesNotExist:
            return Response(
                {'error':'true', 'message':f'User does not exist: {email}'},
                status=status.HTTP_400_BAD_REQUEST
            )

