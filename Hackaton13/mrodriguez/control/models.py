from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User


class IdCardType(models.Model):
    id = models.AutoField(primary_key=True)
    id_card_type = models.CharField(max_length=100, null=True)
    creation_date = models.DateField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id_card_type)


class Sex(models.Model):
    id = models.AutoField(primary_key=True)
    sex = models.CharField(max_length=20, null=True)
    creation_date = models.DateField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.sex)


class Nationality(models.Model):
    id = models.AutoField(primary_key=True)
    country = models.CharField(max_length=100)
    creation_date = models.DateField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.country)


class Student(models.Model):
    id = models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=200, null=False, default="")
    id_card_type = models.ForeignKey(IdCardType, on_delete=models.CASCADE, null=True)
    id_card_number = models.CharField(max_length=20)
    age = models.IntegerField(blank=True, null=True)
    sex = models.ForeignKey(Sex, on_delete=models.CASCADE, null=True)
    nationality = models.ForeignKey(Nationality, on_delete=models.CASCADE, null=True)
    email = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    creation_date = models.DateField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.fullname)


class Teacher(models.Model):
    id = models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=200, default="")
    id_card_type = models.ForeignKey(IdCardType, on_delete=models.CASCADE, null=True)
    id_card_number = models.CharField(max_length=20)
    age = models.IntegerField(blank=True, null=True)
    sex = models.ForeignKey(Sex, on_delete=models.CASCADE, null=True)
    nationality = models.ForeignKey(Nationality, on_delete=models.CASCADE, null=True)
    email = models.CharField(max_length=100)
    # course = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    creation_date = models.DateField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.fullname)


class Course(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, default="")
    description = models.CharField(max_length=200, null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    creation_date = models.DateField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)


class Classroom(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, default="")
    max_students = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1)]
    )

    def __str__(self):
        return str(self.name)


class Enrollment(models.Model):
    id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
    classroom = models.ForeignKey(Classroom, on_delete=models.DO_NOTHING)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    creation_date = models.DateField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.creation_date)


class Day(models.Model):
    id = models.AutoField(primary_key=True)
    day = models.CharField(max_length=100)
    creation_date = models.DateField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.day)


class GradeRecord(models.Model):
    id = models.AutoField(primary_key=True)
    classroom = models.ForeignKey(Classroom, on_delete=models.DO_NOTHING)
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
    day = models.ForeignKey(Day, on_delete=models.CASCADE, null=True)
    grade = models.DecimalField(max_digits=4, decimal_places=1)
    created_by = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING)
    creation_date = models.DateField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.grade)


class Attendance(models.Model):
    id = models.AutoField(primary_key=True)
    attendance = models.CharField(max_length=100)
    creation_date = models.DateField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.attendance)


class AttendanceRecord(models.Model):
    id = models.AutoField(primary_key=True)
    classroom = models.ForeignKey(Classroom, on_delete=models.DO_NOTHING)
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    day = models.ForeignKey(Day, on_delete=models.CASCADE, null=True)
    attendance = models.ForeignKey(Attendance, on_delete=models.CASCADE, null=True)
    created_by = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING)
    creation_date = models.DateField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.attendance)


class Request(models.Model):
    id = models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=200, null=False, default="")
    id_card_type = models.ForeignKey(IdCardType, on_delete=models.CASCADE, null=True)
    id_card_number = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    phone = models.BigIntegerField(blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING, null=True)
    description = models.CharField(max_length=200, null=True)
    creation_date = models.DateField(default=timezone.now)

    def __str__(self):
        return str(self.fullname)
