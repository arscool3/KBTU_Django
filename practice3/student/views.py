from django.shortcuts import render

# Create your views here.
def student_list(request):
    students = [
      'Айгерім', 
      'Айдана', 
      'Айжан', 
      'Айнұр', 
      'Айсерік', 
      'Айтолға', 
      'Айша', 
      'Акбота', 
      'Акжол', 
      'Акмарал'
    ] 
    return render(request, 'students.html', {'students': students})