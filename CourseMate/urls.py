"""
URL configuration for Course_Registration project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Login_and_SignUp.views import *
from Dashboard.views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
     path('', home_page, name='home_page'),
       path('admin/', admin.site.urls),
       path('student-signup/', student_signup_page, name='student_signup_page'),
       path('student-login/', student_login_page, name='student_login_page'),
       path('faculty-signup/', faculty_signup_page, name='faculty_signup_page'),
       path('faculty-login/', faculty_login_page, name='faculty_login_page'),
       path('admin-login/', admin_login_page, name='admin_login_page'),
       path('faculty-dashboard/',faculty_dashboard_page, name='faculty_dashboard_page'),
       path('student-dashboard/',student_dashboard_page, name='student_dashboard_page'),
       path('admin-dashboard/',admin_dashboard_page, name='admin_dashboard_page'),
       path('download/str:<code>',download, name='download'),
       path('add_to_cart/str:<code>',add_to_cart, name='add_to_cart'),
       path('remove_from_cart/str:<code>',remove_from_cart, name='remove_from_cart'),
       path('submit/',submit, name='submit'),
       path('student-enrollments/str:<code>',student_enrollments_page, name='student_enrollments_page'),
       path('approve/<str:email>/str:<code>', approve, name='approve'),
       path('reject/str:<email>/str:<code>',reject, name='reject'),
       path('course_details/str:<code>',course_details, name='course_details'),
       path('add-course/',add_course, name='add_course'),
       path('edit-course/<str:code>',edit_course, name='edit_course'),
       path('remove-course/',remove_course, name='remove_course'),
       path('update/<str:code>',update, name='update'),
       path('logout/', logout_page, name='logout_page'),      
         ]   
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)