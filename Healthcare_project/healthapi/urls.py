from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from .views import (
    RegisterView, PatientListCreateView, PatientDetailView,
    DoctorListCreateView, DoctorDetailView,
    MappingCreateView, MappingListView, PatientDoctorsView, MappingDeleteView
)

urlpatterns = [
    path('auth/register/', RegisterView.as_view()),
    path('auth/login/', TokenObtainPairView.as_view()),

    path('patients/', PatientListCreateView.as_view()),
    path('patients/<int:pk>/', PatientDetailView.as_view()),

    path('doctors/', DoctorListCreateView.as_view()),
    path('doctors/<int:pk>/', DoctorDetailView.as_view()),

    path('mapping/', MappingListView.as_view()),
    path('mapping/create/', MappingCreateView.as_view()),
    path('mappings/<int:patient_id>/', PatientDoctorsView.as_view()),
    path('mappings/delete/<int:id>/', MappingDeleteView.as_view()),
]