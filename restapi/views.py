from django.shortcuts import render
from rest_framework import viewsets
from .serializers import EmployerSerializer
from .models import Employer

class EmployerViewset(viewsets.ModelViewSet):
    queryset = Employer.objects.all().order_by('firstname')
    serializer_class = EmployerSerializer
