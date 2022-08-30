from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class UserModel(AbstractUser):
    class Meta:
        db_table = "auth_user"
        verbose_name = "user"
        verbose_name_plural = "users"

    def get_absolute_url(self):
        return reverse("user:user", kwargs={"slug": self.username})
