from rest_framework import serializers
from .models import *

class LandRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = LandRecord
        fields = '__all__'
