from rest_framework import serializers
from authAppCourier.models.user import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password", "name", "lastName", "email", "state"]
