from django.urls import path
from .views import stipendia_students_view, non_stipendia_students_view, fit_students_view, bs_students_view, studentVIew, home


urlpatterns = [
    path('stipendia_student/', stipendia_students_view, name='stipendia-student'),
    path('non_stipendia_student/', non_stipendia_students_view, name='nonstipendia-student'),
    path('fit/', fit_students_view, name='fit-student'),
    path('bs/', bs_students_view, name='bs-student'),
    path('student/', studentVIew, name='student'),
    path('home/', home, name='home'),
]