from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from django.contrib.auth.models import User


from .models import Product, Profile


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ' __all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name']
        extra_kwargs = {'password': {'write_only': True}}
class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Profile
        fields = ['user', 'age', 'password']

    def create(self, validater_data):
        user_data = validater_data.pop('user')
        user_data['password'] = make_password(user_data['password'])
        user = User.objects.create(**user_data)
        profile = Profile.objects.create(user=user, **validater_data)
        return profile