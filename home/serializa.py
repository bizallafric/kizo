from rest_framework import serializers
from .models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate

class  CreateUserSerializer(serializers.Serializer): 
    phone  = serializers.IntegerField(required=True) 
    name  = serializers.CharField(required=True)
    
        

