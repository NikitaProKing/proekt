from django.shortcuts import render
from rest_framework import generics, status
from django.contrib.auth.models import User
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer, ProfileSerializer


class ProductView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = []

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            data = {
                'user_id': user.id,
                'message': 'User  registered successfully'
            }
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)