from rest_framework import serializers
from .models import UserDetails

# class UserDetailsSerializer(serializers.Serializer):
#     username = serializers.CharField(max_length=50)
#     email = serializers.EmailField(max_length=100)  
#     password = serializers.CharField(max_length=12, required=False)


class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetails
        fields = ['username', 'email', 'password']
