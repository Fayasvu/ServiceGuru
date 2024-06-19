from rest_framework import serializers
from Api.models import Customer


class Customerserializer(serializers.ModelSerializer):

    technician=serializers.StringRelatedField(read_only=True)

    class Meta:
        
        model=Customer
        fields="__all__"
        read_only_fields=["id","technician","status","created_date","updated_date","is_active"]

        
