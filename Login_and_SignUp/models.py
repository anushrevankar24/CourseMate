from django.db import models
from django.contrib.auth.models import AbstractUser
class CustomUser(AbstractUser):
    role=models.CharField(max_length=100,default='default_role')
    name=models.CharField(max_length=100,default='default_name')
    s_id = models.CharField(max_length=50,default='default_id')
    department = models.CharField(max_length=150,default='default_department')
    program_type = models.CharField(max_length=100,default='default_program_type')
    def __str__(self):
        return self.username


    
    
