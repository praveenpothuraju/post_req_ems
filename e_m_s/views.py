from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
import json
# Create your views here.
file_name="e_m_s/static/emps.json"
def read_data():
    with open(file_name,"r") as f:
       return json.load(f)

def write_data(data):
   with open(file_name,"w") as f:
       json.dump(data,f)

def emp_adding_form(request):
    print("VIEW IS CALLED")
    return render(request,"emp.html")

#  @post view
@api_view(["POST"])
def creating_Emp(request):
    data=request.POST.dict()
    # print(type(data),"from data in postreq")
    datafromjsonfile=read_data()
    datafromjsonfile['employees'].append(data)
    write_data(datafromjsonfile)
    # print(datafromjsonfile,"data from json file")
    return HttpResponse("emp added sucessfully")
