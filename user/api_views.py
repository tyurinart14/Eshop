from .models import UserModel
from .serializer import UserSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView


class UserListCreateAPIView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()


class UserDetailUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    lookup_field = 'username'
    queryset = UserModel.objects.all()
