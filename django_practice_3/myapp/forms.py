from django import forms

from myapp.models import Lesson, Student, Teacher


class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = '__all__'


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'