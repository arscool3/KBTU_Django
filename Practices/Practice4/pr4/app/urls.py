from django.urls import path
from .views import *

urlpatterns = [
    path('addPersons/', add_person, name='AddPerson'),
    path('addFamily/', add_family, name='AddFamily'),
    path('addDoctor/', add_doctor, name='AddDoctor'),
    path('addHospital/', add_hospital, name='AddHospital'),

    path('getAllPerson/', showPersons),
    path('getAllFamily/', showFamily),
    path('getAllDoctors/', showDoctor),
    path('getAllHospital/', showHospital),

    path('getPersons_byFamily/<int:f_id>', showPersons_byFamily),
    path('getPersons_by/<int:age>', showPersons_byAge),
    path('getPerson/<int:p_id>', showPerson),

    path('getDoctors_byHospital/<int:h_id>/', showDoctor_byHospital),
    path('getDoctor/<int:d_id>/', showDoctor),
]