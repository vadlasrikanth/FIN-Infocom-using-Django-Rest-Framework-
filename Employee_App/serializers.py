from rest_framework import serializers
from .models import Employee,Address, Workexp
from drf_writable_nested import WritableNestedModelSerializer
from rest_framework.validators import UniqueValidator



class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

class WorkexpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workexp
        fields = '__all__'

class EmployeeSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    addressDetails = AddressSerializer(many=True)
    workExperience = WorkexpSerializer(many=True)
    class Meta:
        model = Employee
        fields = '__all__'

# def create(self, validated_data):
#         addressDetails = validated_data.pop('addressDetails')
#         workExperience = validated_data.pop('workExperience')
#         emails = Employee.objects.filter(email=validated_data['email'])
#         # print(validated_data['email'])
#         if emails:
#             raise serializers.ValidationError("Email Already Exists")
       
#         employee_instance = Employee.objects.create(**validated_data)
#         for address in addressDetails:
#             Address.objects.create(emp=employee_instance,**address)

#         for work in workExperience:
#             Workexp.objects.create(emp=employee_instance,**work)
            
#         return employee_instance
    
def update(self, instance, validated_data):
    addressDetails_list = validated_data.pop('addressDetails')
    instance.name = validated_data.get('name', instance.name)
    instance.phoneNo = validated_data.get('phoneNo', instance.phoneNo)
    instance.email = validated_data.get('email', instance.email)
    instance.age = validated_data.get('age', instance.age)
    instance.gender = validated_data.get('gender', instance.gender)
    instance.photo = validated_data.get('photo', instance.photo)
    instance.save()

    # addresss_with_same_employee_instance = Address.objects.filter(emp=instance.pk).values_list('id', flat=True)

    addresss_id_pool = []

    for address in addressDetails_list:
        if "id" in address.keys():
            if Address.objects.filter(id=address['id']).exists():
                address_instance = Address.objects.get(id=address['id'])
                address_instance.hno = address.get('hno', address_instance.hno)
                address_instance.street = address.get('street',address_instance.street)
                address_instance.city = address.get('city', address_instance.city)
                address_instance.state = address.get('state', address_instance.state)
                address_instance.save()
                addresss_id_pool.append(address_instance.id)
            else:
                continue
        else:
            add_instance = Address.objects.create(emp=instance, **address)
            addresss_id_pool.append(add_instance.id)

    return instance    
