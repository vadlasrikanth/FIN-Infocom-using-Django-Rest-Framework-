from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=30)
    phoneNo = models.IntegerField()
    email = models.EmailField()
    age = models.IntegerField()
    gender =models.CharField(max_length=50)
    photo=models.FileField(upload_to='profile/',null=True,blank=True)
    

class Address(models.Model):   
    emp=models.ForeignKey(Employee,on_delete=models.CASCADE,related_name='addressDetails',null=True,blank=True)
    hno = models.IntegerField()
    street = models.TextField()
    city = models.TextField()
    state = models.TextField()
   

class Workexp(models.Model):   
    emp=models.ForeignKey(Employee,on_delete=models.CASCADE,related_name='workExperience',null=True,blank=True)
    companyName = models.TextField()
    fromdate = models.TextField()
    todate = models.TextField()
    address = models.TextField()

