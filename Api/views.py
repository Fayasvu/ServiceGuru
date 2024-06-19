from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import responses
from rest_framework import authentication,permissions
from Api.serializers import Customerserializer
from Api.models import Customer


class Customerviewsetview(ModelViewSet):

    serializer_class=Customerserializer
    queryset=Customer.objects.all()

    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAdminUser]

    
    def perform_create(self, serializer):
        serializer.save(technician=self.request.user)
        
