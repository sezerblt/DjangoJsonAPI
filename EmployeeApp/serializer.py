from dataclasses import field
from rest_framework import serializers
from . models import Departments,Employees

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Departments
        field='__all__'

class EmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employees
        field='__all__'


