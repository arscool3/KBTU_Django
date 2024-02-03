from django.shortcuts import render

# Create your views here.
def student_list(request):
    students = ['Student1', 'Student2', 'Student3', 'Student4', 'Student5', 'Student6', 'Student7', 'Student8', 'Student9', 'Student10'] 
    return render(request, 'students.html', {'students': students})
