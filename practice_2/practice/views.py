from django.shortcuts import render

# Create your views here.
def student_list(request):
    students = ['Yelaman', 'Aldiar', 'Islam', 'Askar', 'Salamat', 'Aika']
    return render(request, 'students.html', {'students': students})

def capitalizer(request):
    return 
