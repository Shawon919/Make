from django.db import models
from django.contrib.auth.models import (AbstractBaseUser,BaseUserManager,PermissionsMixin)



class UserManager(BaseUserManager):
    def create_user(self,email,password=None,**extra_fields):
        if not email:
            raise ValueError('email needs')
        
        email = self.normalize_email(email)
        user = self.model(
            email = email,
            **extra_fields
        )
        user.set_password(password)
        user.save()
        return user
    
    
    def create_superuser(self,email,password=None,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_admin',True)
        
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_admin', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser must have is_staff=True")
        if extra_fields.get('is_admin') is not True:
            raise ValueError("Superuser must have is_admin=True")

        return self.create_user(email, password, **extra_fields)



class User(AbstractBaseUser,PermissionsMixin):
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    
    
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    mobile = models.CharField(max_length=11)
    profile_picture = models.ImageField(upload_to='profile_pics/', default='blank.jpg')
    
    
    
    
    create_at = models.DateTimeField(auto_now_add=True)
    create_at = models.DateTimeField(auto_now=True)
    
    otp = models.CharField(max_length=4)
    
    def __str__(self):
        return self.email
    
    objects = UserManager()
    
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name']
    
    
    def has_perm(self, perm, obj=None):
        return self.is_admin  

    def has_module_perms(self, app_label):
        
        return True 
    
        
    
    
    

    
    
    
