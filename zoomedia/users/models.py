from django.db import models
from zoomedia.common.models import BaseModel

from django.contrib.auth.models import AbstractBaseUser , AbstractUser
from django.contrib.auth.models import BaseUserManager as BUM
from django.contrib.auth.models import PermissionsMixin



class BaseUserManager(BUM):
    def create_user(self, email,username , is_active=True , is_admin=False, password=None):
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(email=self.normalize_email(email.lower()), username=username, is_active=is_active, is_admin=is_admin)

        if password is not None:
            user.set_password(password)
        else:
            user.set_unusable_password()

        user.full_clean()
        user.save(using=self._db)

        return user

    def create_superuser(self, email, username ,  password=None):
        user = self.create_user(
            email=email,
            username=username,
            is_active=True,
            is_admin=True,
            password=password,
        )

        user.is_superuser = True
        user.save(using=self._db)

        return user


class BaseUser(BaseModel, AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(verbose_name = "email address",
                              unique=True)

    username = models.CharField(max_length=255 , unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    
    objects = BaseUserManager()

    USERNAME_FIELD = "username"

    def __str__(self):
        return self.username

    def is_staff(self):
        return self.is_admin
    
    








