from .models import UserModel
from .serializer import UserSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView


class UserListCreateAPIView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()


class UserDetailUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    model = serializer_class.Meta.model

    def get_queryset(self):
        user_id = self.kwargs['id']
        queryset = self.model.objects.get(id=user_id)
        return queryset
