from django import forms

from core.models import Book, Student, Teacher, Admin


class BookForm(forms.ModelForm ):
    class Meta:
        model = Book
        fields = '__all__'
    def save(self, commit=True):
        book = super().save(commit=False)
        if commit:
            book.save()
            # Increment the book counter for the associated student
            student = book.student
            student.book_count += 1
            student.save()
        return book


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'

class AdminForm(forms.ModelForm):
    class Meta:
        model = Admin
        fields = '__all__'