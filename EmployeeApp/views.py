from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from .models import Departments,Employees
from .serializer import DepartmentSerializer,EmployeesSerializer

def index(reuest):
    return HttpResponse("index Page")

@csrf_exempt
def departmentApi(request,id=0):
    if request.method=='GET':
        departments = Departments.objects.all()
        department_serializer =DepartmentSerializer(departments,many=True)
        return JsonResponse(department_serializer.data,safe=False)
    elif request.nethod=='POST':
        department_data =JSONParser().parse(request)
        department_serializer=DepartmentSerializer(data=department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("Eklendi",safe=False)
        return JsonResponse("Eklenmedi",safe=False)
    elif request.method=='PUT':
        department_data=JSONParser().parse(request)
        department = Departments.objects.get(DepartmentsId=department_data['DepartmentsId'])
        department_serializer=DepartmentSerializer(department,data=department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("Guncellendi",safe=False)
        return JsonResponse("Guncelenmedi",safe=False)
    elif request.method=='DELETE':
        departments = Departments.objects.get(DepartmentsId=id)
        departments.delete()
        return JsonResponse("Silindi",safe=False)