from django.shortcuts import render
from .models import Employee
from django.views.generic import View
from django.http import HttpResponse
# Create your views here.
import json
from django.core.serializers import serialize
class EmployeeDetailCBV(View):
    def get(self,request,*args,**kwargs):
        emp=Employee.objects.get(id=3)
        json_data=serialize('json',[emp,])
        return HttpResponse(json_data,content_type='application/json')