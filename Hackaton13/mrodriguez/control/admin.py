from django.contrib import admin

from .models import (
    Student,
    Teacher,
    # Cicle,
    Course,
    Classroom,
    Enrollment,
    IdCardType,
    Nationality,
    Sex,
    GradeRecord,
    Attendance,
    AttendanceRecord,
    Day,
    Request,
)

admin.site.register(Student)
admin.site.register(Teacher)
# admin.site.register(Cicle)
admin.site.register(Course)
admin.site.register(Classroom)
admin.site.register(Enrollment)
admin.site.register(IdCardType)
admin.site.register(Nationality)
admin.site.register(Sex)
admin.site.register(GradeRecord)
admin.site.register(Attendance)
admin.site.register(AttendanceRecord)
admin.site.register(Day)
admin.site.register(Request)
