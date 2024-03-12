from django.shortcuts import render

def stydent_list(request):
    students = [
        {'name': 'Muktarkhan' , 'age' : 19}
        {'name' : 'Zhadi' , 'age' : 20}
        {'name' : 'Bek' , 'age' : 18}

    ] 
    return render(request , 'studentlist/student_list.html' , {'students' : students})
