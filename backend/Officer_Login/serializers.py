from rest_framework import serializers
from .models import *

class Officer_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Officer
        fields = "__all__"
