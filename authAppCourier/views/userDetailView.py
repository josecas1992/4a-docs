from rest_framework import generics

from authAppCourier.models.user import User
from authAppCourier.serializers.userSerializer import UserSerializer


class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
