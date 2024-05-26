from django import forms
from app.models import News, Student, Faculty, Speciality, Discipline, Professor, Schedule


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content']


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'surname', 'id', 'gpa', 'speciality', 'course', 'disciplines', 'login', 'password']


class FacultyForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = ['name']


class SpecialityForm(forms.ModelForm):
    class Meta:
        model = Speciality
        fields = ['name', 'code', 'faculty']


class DisciplineForm(forms.ModelForm):
    class Meta:
        model = Discipline
        fields = ['name', 'credits', 'code', 'faculty', 'grade']


class ProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ['name', 'surname', 'year_of_experience', 'degree', 'disciplines', 'login', 'password']


class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['professor', 'student', 'time_slot', 'day', 'discipline']
