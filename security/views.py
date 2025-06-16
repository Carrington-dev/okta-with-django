from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from security.models import User
from security.serializers import UserCreateSerializer

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer

    def get(self, pk=None):
        if pk:
            serializer = UserCreateSerializer(User.objects.get(pk))
            return Response(
                data=serializer.data,
                status=status.HTTP_200_OK
            )
        user_list =  User.objects.all()
        serializer =  UserCreateSerializer(many=True, data=user_list)
        return Response(data=serializer.data, status=status.HTTP_200_OK)