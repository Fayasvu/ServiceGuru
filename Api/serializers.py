from rest_framework import serializers
from Api.models import Customer,work


class Workserializer(serializers.ModelSerializer):

    customer=serializers.StringRelatedField(read_only=True)

    class Meta:

        model=work
        fields="__all__"
        read_only_fields=["id","customer","created_date","updated_date","is_active"]


class Customerserializer(serializers.ModelSerializer):

    technician=serializers.StringRelatedField(read_only=True)

    work_count=serializers.CharField(read_only=True)

    work_totalamount=serializers.CharField(read_only=True)

    class Meta:
        
        model=Customer
        fields="__all__"
        read_only_fields=["id","technician","status","created_date","updated_date","is_active"]

        
