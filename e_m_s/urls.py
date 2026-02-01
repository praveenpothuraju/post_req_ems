from django.urls import path
from .views import emp_adding_form,creating_Emp,getAll_Emps
urlpatterns=[
    path("",emp_adding_form,name='emp'),
    path("api/emp/create/", creating_Emp,name='creating_emp'),
    path("api/emp/get_all_data/", getAll_Emps,name='getAll_emps')
]