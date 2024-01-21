
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.shortcuts import render ,redirect
from Login_and_SignUp.models import CustomUser
from Dashboard.views import *

def home_page(request):
    return render(request, 'home.html')

def logout_page(request):
      logout(request);
      return render(request, 'home.html')

def student_signup_page(request):
    if request.method == 'POST':
        role='student'
        name=request.POST.get('name')
        s_id=request.POST.get('id')
        email=request.POST.get('email') 
        cgpa=request.POST.get('cgpa')   
        program_type=request.POST.get('program_type')
        department= request.POST.get('department')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
        if password != confirm_password:
            messages.error(request,"Confirm password is not same as password")
            return redirect('student_signup_page')
        existing_user = CustomUser.objects.filter(email=email).exists()
        if existing_user:
            messages.error(request, "A user with this email already exists !!!")
            return redirect('student_signup_page')
        
        user = CustomUser.objects.create_user(
              username=email,
               email=email,
               password=password,
              name=name,
              s_id=s_id,
              cgpa=cgpa,
               department=department,
                program_type=program_type,
                role=role
            )
        # user.set_password(password)
        user.save()
        messages.success(request,"Your Account has been Successfully created !!!")
        return redirect('student_login_page')
    return render(request, 'student_signup.html')
     
def faculty_signup_page(request):
    if request.method == 'POST':
        role='faculty'
        name=request.POST.get('name')
        id=request.POST.get('id')
        email=request.POST.get('email')  
        department= request.POST.get('department')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
        if password != confirm_password:
            messages.error(request,"Confirm password is not same as password")
            return redirect('faculty_signup_page')
        existing_user = CustomUser.objects.filter(email=email).exists()
        if existing_user:
            messages.error(request, "A user with this email already exists !!!")
            return redirect('faculty_signup_page')
        
        user = CustomUser.objects.create_user(
               username=email,
               email=email,
               password=password,
              name=name,
              s_id=id,
              program_type='',
               department=department,
               role=role
        )
        user.save()
        messages.success(request,"Your Account has been Successfully created !!!")
        return redirect('faculty_login_page')
    return render(request, 'faculty_signup.html')

def student_login_page(request):
    if request.method =='POST':
        email=request.POST.get('email')  
        password=request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None and user.role=='student':
            login(request, user);
            return redirect('student_dashboard_page')
        else :
            messages.error(request,"Credentials did not match")
            return render(request, 'student_login.html')
            # return redirect('student_login_page')
    return render(request, 'student_login.html')
  
def faculty_login_page(request):
    if request.method =='POST':
        email=request.POST.get('email')  
        password=request.POST.get('password')
        #below line returns None of not None
        user = authenticate(request, username=email, password=password)
        if user is not None and user.role=='faculty':
            login(request, user);
            return redirect('faculty_dashboard_page')
        else :
            messages.error(request,"Credentials did not match")
            return redirect('faculty_login_page')
    return render(request, 'faculty_login.html')
  
def admin_login_page(request):
    if request.method =='POST':
        email=request.POST.get('email')  
        password=request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None and user.role=='admin':
            login(request, user);
            return redirect('admin_dashboard_page')
        else :
            messages.error(request,"Credentials did not match")
            return redirect('admin_login_page')
    return render(request, 'admin_login.html')

