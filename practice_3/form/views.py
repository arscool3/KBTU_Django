from django.shortcuts import render, redirect
from .forms import InputForm
from .models import Student

def home_view(request):
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            # Create a new Student instance
            student = Student()

            # Populate the instance with form data
            student.first_name = form.cleaned_data['first_name']
            student.last_name = form.cleaned_data['last_name']
            student.roll_number = form.cleaned_data['roll_number']
            student.password = form.cleaned_data['password']

            # Save the instance to the database
            student.save()

            # Redirect to a success page or do something else
            return redirect('success')
    else:
        form = InputForm()

    context = {'form': form}
    return render(request, 'home.html', context)

def success_view(request):
    return render(request, 'success.html')