from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import (Registerserializers,Viewserializer,View,Loginserializer)
from .models import User
from django.contrib.auth import authenticate
import random
from django.core.mail import send_mail
from rest_framework_simplejwt.tokens import RefreshToken
import random
from rest_framework.permissions import IsAuthenticated

    
    
        
        
        
class register(APIView):
    def post(self,request):
        serializer = Registerserializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'serializer':serializer.data.get('profile_picture'),'status':'success','message':'user registered successfully'},status=status.HTTP_201_CREATED)
        return Response({'status':' failed','message':'user registered failed'},status=status.HTTP_400_BAD_REQUEST)            
    
 
class Loginview(APIView):
    def post(self,request):
        email = request.data.get('email')
        password = request.data.get('password')
        
        user = authenticate(email=email,password=password)
        
        if user:
            refresh = RefreshToken.for_user(user)
           
            return Response({'status':'success','message':'user login successfully','token':str(refresh.access_token)},status=status.HTTP_200_OK)
        return Response({'status':'failed','message':'user login failed'},status=status.HTTP_201_CREATED)
    
    
    
 
  
class send_otp(APIView):
    def post(self,request):
       serilizer = View(data=request.data)
       if serilizer.is_valid():
           email = serilizer.data['email']
           if User.objects.filter(email=email).exists():
               user = User.objects.get(email=email)
               otp = random.randint(1000,9999)
               user.otp = otp
               user.save()
               send_mail(
                   subject='sending the email',
                   message=f'your opt is {otp}',
                   from_email='don not know',
                   recipient_list=[email]
               )
               return Response({'status':'success','message':'otp send','otp':str(otp)},status=status.HTTP_200_OK)
           return Response({'status':'failed','message':'otp failed'},status=status.HTTP_400_BAD_REQUEST)
       return Response('email is required')
   



class varify_otp(APIView):
    def post(self,request):   
        email = request.data.get('email')
        opt = request.data.get('otp')
        
        if not email and not opt:
            return Response({'message':'given fields are required'})
        
        try:
            user = User.objects.get(email=email)
            if user.otp == opt:
                refresh = RefreshToken.for_user(user)
                return Response({'status':'success','message':'otp send','token':str(refresh.access_token)},status=status.HTTP_200_OK)
            return Response({'status':'failed','message':'otp or email is not valid'},status=status.HTTP_400_BAD_REQUEST)
                
        except User.DoesNotExist:
            return Response({'message':'email or opt is required'},status=status.HTTP_404_NOT_FOUND)
        


class reset_password(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):
        password =  request.data.get('password') 
        user = request.user
        
        if password is None:
            return Response({'message':'password is required'})
        user.set_password(password)
        user.save()
        return Response({'message':'password updated successfully'})
    
    
    
        
                 
            
class getusers(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self,request):
        id = request.data.get('id')
        
        try:
            user = User.objects.get(id=id)
            serializer = Viewserializer(user)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
        
        
class submitemail(APIView):
    def post(self,request):
        email = request.data.get('email')
        if User.objects.filter(email=email).exists():
            try:
                user = User.objects.get(email=email)
                username = user.first_name
                return Response({'status':'success','message':'email found','username':{username}},status=status.HTTP_200_OK)
            
            
            except User.DoesNotExist:
                return Response({'message':'email not found'},status=status.HTTP_404_NOT_FOUND)
                
            
        
        
           
        
    
       