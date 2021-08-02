from django.contrib.auth import authenticate
from rest_framework import serializers 
from django.contrib.auth import hashers

class LoginSerializer(serializers.Serializer): 
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, attrs):

        user = authenticate(email=attrs['email'], password=attrs['password'])

        if not user:
            raise serializers.ValidationError('Incorrect email or password.')

        if not user.is_active:
            raise serializers.ValidationError('User is disabled.')

        return {'user': user}    
    
