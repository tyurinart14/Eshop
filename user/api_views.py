from .models import UserModel
from .serializer import UserSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions
from .permissions import UserProfilePermission


class UserListCreateAPIView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
    permission_classes = [permissions.IsAuthenticated]


class UserDetailUpdateAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    lookup_field = 'username'
    queryset = UserModel.objects.all()
    permission_classes = [UserProfilePermission]
