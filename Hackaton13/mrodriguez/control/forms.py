from django.forms import ModelForm
from .models import Request, GradeRecord, AttendanceRecord


class RequestForm(ModelForm):
    class Meta:
        model = Request
        fields = [
            "fullname",
            "id_card_type",
            "id_card_number",
            "email",
            "phone",
            "course",
            "description",
        ]


class GradeForm(ModelForm):
    class Meta:
        model = GradeRecord
        fields = [
            "classroom",
            "student",
            "course",
            "day",
            "grade",
            "created_by",
        ]


class AttendanceForm(ModelForm):
    class Meta:
        model = AttendanceRecord
        fields = [
            "classroom",
            "course",
            "student",
            "day",
            "attendance",
            "created_by",
        ]
