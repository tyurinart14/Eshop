from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class UserModel(AbstractUser):
    wallet = models.IntegerField()

    class Meta:
        db_table = "auth_user"
        verbose_name = "user"
        verbose_name_plural = "users"

    def get_absolute_url(self):
        return reverse("user:user", kwargs={"slug": self.username})
