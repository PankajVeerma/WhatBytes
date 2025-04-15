from django.db import models

# Create your models here.
class User(models.Model):
  username=models.CharField(max_length=50)
  password=models.CharField(max_length=50)
  email=models.EmailField(unique=True)
  
  
class Patient(models.Model):
  name=models.CharField(max_length=50)
  age=models.IntegerField()
  disease=models.CharField(max_length=100)
  contact=models.CharField(max_length=15)
  address=models.CharField(max_length=200)
  doctor_to_meet=models.CharField(max_length=50)
  date_of_visit=models.DateField()
  
  
class Doctor(models.Model):
  name=models.CharField(max_length=50)
  age=models.IntegerField()
  specialization=models.CharField(max_length=100)
  contact=models.CharField(max_length=15)
  address=models.CharField(max_length=200)
  date_of_joining=models.DateField() 
  
class Mapping(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.patient.name} - {self.doctor.name}"
    

   
   
 
  

