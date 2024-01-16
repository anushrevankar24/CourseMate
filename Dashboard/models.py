from django.db import models
from Login_and_SignUp.models import CustomUser
# Create your models here.
class courses(models.Model):
    email = models.CharField(max_length=100)
    code=models.CharField(max_length=100)
    title=models.CharField(max_length=150)
    department = models.CharField(max_length=150)
    details=models.TextField(default='default_details')
    instructor=models.CharField(max_length=100)
    credits=models.IntegerField()
    cgpa=models.DecimalField(decimal_places=2, max_digits=3, default=7.00)
    slots=models.IntegerField()
    filled_slots=models.IntegerField(default=0)
    schedule = models.FileField(upload_to='schedules/')
    program_type = models.CharField(max_length=100)
    def __str__(self):
        return self.code

class Cart(models.Model):
    # user=models.ForeignKey(CustomUser,on_delete=models.CASCADE , related_name='cart')
    user=models.OneToOneField(CustomUser,on_delete=models.CASCADE , related_name='cart')
    def __str__(self):
        return self.user.email

class CartItems(models.Model):
        cart=models.ForeignKey(Cart,on_delete=models.CASCADE , related_name='cart_items')
        course=models.ForeignKey(courses,on_delete=models.CASCADE ,related_name='course_in_cart',null=True)
        def __str__(self):
            return f"{self.cart.user.email}-{self.course.code}"
          
class enrollment(models.Model):
    student=models.ForeignKey(CustomUser,on_delete=models.CASCADE , related_name='student')
    course=models.ForeignKey(courses,on_delete=models.CASCADE , related_name='course')
    status=models.CharField(max_length=100, default='Request')
    def __str__(self):
        return f"{self.student.email} - {self.course.code}"
    
    
        
    
