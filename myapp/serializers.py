from rest_framework import serializers
from myapp.models import *

class User_Serializer(serializers.ModelSerializer):
    # Employee_id = serializers.CharField(required=False)
    Name=serializers.CharField(required=False)
    Rank=serializers.FloatField(required=False)
    class Meta:
        model=User
        fields='__all__'

