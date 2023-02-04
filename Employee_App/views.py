from rest_framework.response import Response
from rest_framework import viewsets
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework import serializers
from .models import Employee,Address, Workexp

# Create your views here.
class EmployeeViewset(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    http_method_names = ['get','post','retrieve','put','delete']
    


    def create(self, validated_data):
        addressDetails = validated_data.pop('addressDetails')
        workExperience = validated_data.pop('workExperience')
        emails = Employee.objects.filter(email=validated_data['email'])
        
        if emails:
            raise serializers.ValidationError("Email Already Exists")
       
        employee_instance = Employee.objects.create(**validated_data)
        for address in addressDetails:
            Address.objects.create(emp=employee_instance,**address)

        for work in workExperience:
            Workexp.objects.create(emp=employee_instance,**work)
            
        return employee_instance
    

    def destroy(self, request, *args, **kwargs):
        user_object = self.get_object()
        Employee.objects.filter(id=user_object.id).delete()
        user_object.delete()
        return Response({"status_code": 200, "data": "Deleted Successfully"})    