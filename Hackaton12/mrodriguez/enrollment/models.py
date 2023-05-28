from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User


class Student(models.Model):
    fullname = models.CharField(max_length=200, null=False, default="")
    id_card = models.BigIntegerField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=200)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    created_date = models.DateField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.fullname)


class Cicle(models.Model):
    name = models.CharField(max_length=200)
    created_date = models.DateField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)


class Teacher(models.Model):
    fullname = models.CharField(max_length=200, null=False, default="")
    id_card = models.BigIntegerField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=200)
    # course = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    created_date = models.DateField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.fullname)


class Course(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200, null=True)
    cicle = models.ForeignKey(Cicle, on_delete=models.DO_NOTHING)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    created_date = models.DateField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING)
    # image = models.ImageField(upload_to="uploads/")

    def __str__(self):
        return str(self.name)


class Classroom(models.Model):
    name = models.CharField(max_length=200, null=False, default="")
    cicle = models.ForeignKey(Cicle, on_delete=models.DO_NOTHING)
    max_students = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1)]
    )

    def __str__(self):
        return str(self.name)


class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    teacher = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING)
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
    cicle = models.ForeignKey(Cicle, on_delete=models.DO_NOTHING)
    classroom = models.ForeignKey(Classroom, on_delete=models.DO_NOTHING)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    created_date = models.DateField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.created_date)


class Request(models.Model):
    fullname = models.CharField(max_length=200, null=False, default="")
    id_card = models.BigIntegerField(blank=True, null=True)
    email = models.CharField(max_length=200)
    phone = models.BigIntegerField(blank=True, null=True)
    description = models.CharField(max_length=200, null=True)
    created_date = models.DateField(default=timezone.now)

    def __str__(self):
        return str(self.fullname)
