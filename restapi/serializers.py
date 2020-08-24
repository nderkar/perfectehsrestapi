from rest_framework import serializers
from .models import Employer

class EmployerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employer
        fields = ('firstname', 'lastname')
