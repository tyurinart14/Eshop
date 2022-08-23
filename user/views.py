from django.contrib.auth.views import LoginView
from django.http import HttpRequest, HttpResponseRedirect

from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.views.generic import CreateView, DetailView, UpdateView

from user.forms import RegisterForm, LoginForm
from user.models import UserModel


class ClientPage(DetailView):
    model = UserModel
    template_name = "client_page.html"

    def get_object(self, **kwargs):
        return UserModel.objects.get(username=self.kwargs["slug"])


class ClientUpdateView(UpdateView):
    model = UserModel
    form_class = RegisterForm
    template_name = "register_page.html"

    def get_object(self, **kwargs):
        return UserModel.objects.get(username=self.kwargs["slug"])


class LoginPageView(LoginView):
    form_class = LoginForm
    model = UserModel
    template_name = "login_page.html"


class RegisterPageView(CreateView):
    form_class = RegisterForm
    model = UserModel
    template_name = "register_page.html"


def logout_view(request: HttpRequest):
    logout(request)
    return HttpResponseRedirect(reverse_lazy("homepage"))
