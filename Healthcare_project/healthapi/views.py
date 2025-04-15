from rest_framework import generics, permissions
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import Patient, Doctor, Mapping
from .serializers import (
    RegisterSerializer, PatientSerializer, DoctorSerializer, MappingSerializer
)

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class PatientListCreateView(generics.ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_permissions(self):
        self.permission_classes=[AllowAny]
        if self.request.method =='POST':
            self.permission_classes=[permissions.IsAuthenticated]
        return super().get_permissions()

class PatientDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    
    

class DoctorListCreateView(generics.ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_permissions(self):
        self.permission_classes=[AllowAny]
        if self.request.method =='POST':
            self.permission_classes=[permissions.IsAuthenticated]
        return super().get_permissions()

class DoctorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    
    
    

class MappingCreateView(generics.CreateAPIView):
    serializer_class = MappingSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Mapping.objects.all()

class MappingListView(generics.ListAPIView):
    
    queryset = Mapping.objects.all()
    serializer_class = MappingSerializer
    permission_classes = [permissions.IsAuthenticated]

class PatientDoctorsView(generics.ListAPIView):
    serializer_class = MappingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        patient_id = self.kwargs['patient_id']
        return Mapping.objects.filter(patient_id=patient_id)

class MappingDeleteView(generics.DestroyAPIView):
    queryset = Mapping.objects.all()
    serializer_class = MappingSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'