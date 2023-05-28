from django.contrib import admin

from .models import Student, Teacher, Cicle, Course, Classroom, Enrollment, Request

# Register your models here.
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Cicle)
admin.site.register(Course)
admin.site.register(Classroom)
admin.site.register(Enrollment)
admin.site.register(Request)
