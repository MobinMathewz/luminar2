from django.urls import path
from Students.views import *

urlpatterns=[
    path("reg/",CreateStudent.as_view(),name="register"),
    path("list/",ListStudent.as_view(),name="listStud"),
    path('update/<int:pk>',UpdateStudent.as_view(),name="updateStud"),
    path('delete/<int:pk>',StudentDelete.as_view(),name='deleteStud'),
]