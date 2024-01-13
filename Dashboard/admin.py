from django.contrib import admin
from .models import courses, Cart,CartItems,enrollment

class CourseAdmin(admin.ModelAdmin):
     list= ('code', 'title', 'instructor', 'credits', 'department','slots', 'details','program_type','schedule')
class CartAdmin(admin.ModelAdmin):
     list=('user')
class CartItemsAdmin(admin.ModelAdmin):
     list=('user','code')
class enrollmentAdmin(admin.ModelAdmin):
     list=('student','course','status')
admin.site.register(courses,CourseAdmin)
admin.site.register(Cart,CartAdmin)
admin.site.register(CartItems,CartItemsAdmin)
admin.site.register(enrollment,enrollmentAdmin)


# Register your models here.
