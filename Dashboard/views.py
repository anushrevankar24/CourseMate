import os
from django.conf import settings
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import render ,redirect
from Dashboard.models import courses,Cart,CartItems,enrollment
from Login_and_SignUp.models import CustomUser
from django.contrib.auth.decorators import login_required
from decouple import config
from django.core.mail import send_mail


@login_required(login_url='faculty-login/')
def faculty_dashboard_page(request):
    courses = courses_list(request)
    data={
        'courses': courses,
    }
    return render(request,'faculty_dashboard.html',data)

@login_required(login_url='student-login/')
def student_dashboard_page(request):
    courses = courses_list(request)
    cart_items = course_cart(request)
    submissions = submission(request)
    data = {
       'courses': courses,
       'cart_items': cart_items,
       'submissions': submissions,
    }
    return render(request,'student_dashboard.html',data)

@login_required(login_url='admin-login/')
def admin_dashboard_page(request):
    courses = courses_list(request)
    data={
        'courses': courses,
    }
    return render(request,'admin_dashboard.html',data)

def courses_list(request):
    user = request.user
    if(user.role=='faculty'):
        courses_list=courses.objects.filter(email=user.email).values()
    elif(user.role=='admin'):
        courses_list=courses.objects.all().values()
    else:
       courses_list=courses.objects.filter(program_type=user.program_type).values()
    return courses_list

def course_cart(request):
    user = request.user
    cart, _ =Cart.objects.get_or_create(user=user)
    cart_items = (
            CartItems.objects
            .filter(cart=cart)
            .select_related('course').exclude(course__isnull=True)
        )
    return cart_items

def course_details(request,code):
    course=courses.objects.values().get(code=code)
    data={
        'course':course
    }
    return render(request, 'view_course.html',data)
       
def submission(request):
    user=request.user
    submissions=enrollment.objects.filter(student=user)
    return submissions
    
def add_to_cart(request,code):
    course=courses.objects.get(code=code)
    user=request.user
    cart, _ =Cart.objects.get_or_create(user=user)
    if(CartItems.objects.filter(cart=cart,course=course).exists()):
         messages.error(request,f"{course.code} course is already present in your cart")
    else:
        CartItems.objects.create(cart=cart,course=course)
        messages.success(request,f"{course.code} course sucessfully added to your cart")
    return redirect('student_dashboard_page')


def remove_from_cart(request,code):
    course=courses.objects.get(code=code)
    user=request.user
    cart=Cart.objects.get(user=user)
    cart_item=CartItems.objects.get(cart=cart,course=course)
    cart_item.delete()
    return redirect('student_dashboard_page')

def submit(request):
    cart_items = course_cart(request)
    student=request.user
    for item in cart_items:
        submitted_course=item.course
        if(enrollment.objects.filter(student=student,course=submitted_course,status='Requested').exists()
             ):
            messages.error(request,f"{submitted_course.code} is already been submitted , Please remove it to procced further")
            return redirect('student_dashboard_page')
        else:
            status='Requested'
            e=enrollment(student=student,course=submitted_course,status=status)
            e.save()
            item.delete()
    messages.success(request, "Enrollment request submitted to the instructors successfully.")
    EMAIL_HOST_USER = config('EMAIL_HOST_USER')
    from_email = f"CourseMate <{EMAIL_HOST_USER}>"
    # from_email = "emailnotifications07.noreply@gmail.com"
    email_subject = "Course Submission Successfull"
    email_body = (
            "You have successfully submitted the enrollment request to the course instructors.\n\n\n"
           "This is an automated message. Please do not reply to this email.\n\n"
           "Regards\n"
            "Team CourseMate\n"
              )
    try:
       send_mail(
          email_subject,
          email_body,
          from_email,
          [student.email],
          fail_silently=False,
            )  
    except Exception as e:
       messages.error(request, f"Failed to send email: {str(e)}")
    return redirect('student_dashboard_page')
 
def approve(request,email,code):
    course =courses.objects.get(code=code)
    student=CustomUser.objects.get(email=email)
    course.filled_slots=course.filled_slots+1
    courses.objects.filter(code=course.code).update(filled_slots=course.filled_slots)
    e=enrollment.objects.filter(student=student,course=course,status='Requested').update(status='Accepted')
    EMAIL_HOST_USER = config('EMAIL_HOST_USER')
    from_email = f"CourseMate <{EMAIL_HOST_USER}>"
    # from_email = f"Do not reply to this email (via CRS) <emailnotifications07.noreply@gmail.com>"
    email_subject = "Course enrollment request Accepted"
    email_body = (
            f"{course.code} course instructor has accepted your enroll request. You have been successfully enrolled in the {course.code} course\n\n\n"
            
           "This is an automated message. Please do not reply to this email.\n"
           
           "Regards\n"
            "Team CourseMate\n"
              )
    try:
       send_mail(
          email_subject,
          email_body,
          from_email,
          [student.email],
          fail_silently=False,
            ) 
    except Exception as e:
       messages.error(request, f"Failed to send email: {str(e)}")
    return redirect('student_enrollments_page',code)

def reject(request,email,code):
    course =courses.objects.get(code=code)
    student=CustomUser.objects.get(email=email)
    e=enrollment.objects.filter(student=student,course=course,status='Requested').update(status='Rejected')
    return redirect('student_enrollments_page',code)

def download(request, code):
    course =courses.objects.get(code=code)
    path=course.schedule.path
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/pdf")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404

def student_enrollments_page(request,code):
    course =courses.objects.get(code=code)
    requests=enrollment.objects.filter(course=course,status="Requested")
    enrollments=enrollment.objects.filter(course=course,status="Accepted")
    data={
        'requests':requests,
        'enrollments':enrollments
    }
    return render(request ,'student_enrollments.html',data)
        
def add_course(request):
  if request.method == 'POST':
      user=request.user
      if(user.role=='faculty'):
          email = user.email
          department =user.department
          instructor=user.name 
      else :
          email = request.POST.get('email')
          department =request.POST.get('department')
          instructor=request.POST.get('instructor')
      code=request.POST.get('code')
      title=request.POST.get('title')
      details=request.POST.get('details')
      credits=request.POST.get('credits')
      slots=request.POST.get('slots')
      cgpa=request.POST.get('cgpa')
      schedule = request.FILES.get('schedule') 
      program_type=request.POST.get('program_type')
      course=courses(email=email,
                      code=code,
                      title=title,
                      instructor=instructor,
                      credits=credits,
                      slots=slots,
                      cgpa=cgpa,
                      schedule=schedule,
                      program_type=program_type, 
                      department=department,
                      details=details,)
      course.save()
      messages.success(request,"New Course added Successfully !!! ")  
      return redirect('faculty_dashboard_page')
   
def edit_course(request,code):
    course=courses.objects.values().get(code=code)
    data={
        'course':course
    }
    return render(request, 'edit_course.html',data)
    
def update(request,code):
    if request.method == 'POST':
       email = request.user.email
       code=request.POST.get('code')
       title=request.POST.get('title')
       department =request.user.department
       details=request.POST.get('details')
       instructor=request.user.name
       credits=request.POST.get('credits')
       slots=request.POST.get('slots')
       schedule = request.FILES.get('schedule') 
       program_type=request.POST.get('program_type')
       courses.objects.filter(code=code).update(email=email,
                      code=code,
                      title=title,
                      instructor=instructor,
                      credits=credits,
                      slots=slots,
                      schedule=schedule,
                      program_type=program_type, 
                      department=department,
                      details=details)
    
       messages.success(request,"Course details updated Successfully !!! ")  
       return redirect('edit_course')
   
   
def remove_course(request,code,title):
    if(courses.objects.get(code=code,title=title).exists()):
         course=courses.objects.get(code=code,title=title)
         user=request.user
         cart_items=CartItems.objects.filter(course=course)
         cart_items.delete()
         course.delete()
         messages.success(request,f"{code} Course removed Successfully !!! ") 
    else:
        messages.error(request,"Course not found !! Please enter correct details")
    return redirect('admin_dashboard_page')
