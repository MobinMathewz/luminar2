from django.forms import ModelForm
from Students.models import Student

class StudentCreationForm(ModelForm):
    class Meta:
        model=Student
        fields= ["roll","name","course","address","username","password"]


class StudentUpdateForm(ModelForm):
    class Meta:
        model=Student
        fields= ["name","course","address","password"]