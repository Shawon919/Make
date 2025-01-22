from rest_framework.serializers import ModelSerializer
from .models import (User)
from rest_framework import serializers


class Registerserializers(ModelSerializer):
    class Meta:
        model = User 
        fields = ("first_name", "last_name", "email", "password", "mobile","profile_picture")
        extra_kwargs = {'password': {'write_only': True}}  

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)  
        return user
    
    
    
class Viewserializer(ModelSerializer):
         class Meta:
             model = User 
             fields = ("__all__")
        


    
class View(serializers.Serializer):
        email = serializers.EmailField()
        
        
class Loginserializer(serializers.Serializer):
    email = serializers.EmailField()     
    password = serializers.CharField()   
    
    
    

       