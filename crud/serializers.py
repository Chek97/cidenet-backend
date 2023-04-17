from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id', 'first_name', 'other_name', 'last_name', 'job_country', 'email')
        # TODO: debo hacer que el email lo cree con lo que recibe