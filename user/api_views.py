from .models import UserModel
from .serializer import UserSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class UserListCreateAPIView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()


class UserDetailUpdateAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    lookup_field = 'username'
    queryset = UserModel.objects.all()
