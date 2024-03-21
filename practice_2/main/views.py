from django.shortcuts import render

students = [
  {
    "name": "Bekarys",
    "id": "21BD030887",
  },
  {
    "name": "Andrew",
    "id": "22BD030887",
  },
  {
    "name": "Alma",
    "id": "21BD050307",
  },
  {
    "name": "Erkezhan",
    "id": "22MD045673",
  },
  {
    "name": "Bekzhan",
    "id": "20MD000012",
  },
]

def my_view(request):
  return render(request, 'index.html', {'students': students})