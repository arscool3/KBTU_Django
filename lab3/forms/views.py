# views.py
from django.shortcuts import render, redirect
from .forms import StudentForm

def student_form(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirect to a success page
    else:
        form = StudentForm()
    return render(request, 'student_form.html', {'form': form})
# views.py


def success_page(request):
    return render(request, 'success.html')  # Render the success page template
