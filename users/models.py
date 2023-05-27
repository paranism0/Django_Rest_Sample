from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.contrib.auth.hashers import make_password

# Create your models here.

class UserManager(UserManager):
    def _create_user(self, number, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not number:
            raise ValueError('The given number must be set')
  
        user = self.model( number=number, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, number=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user( number, password, **extra_fields)

    def create_superuser(self, number, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user( number, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=255)
    family = models.CharField(max_length=255)
    number = models.CharField(max_length=13 , unique=True)
    password = models.CharField(max_length=50)
    is_staff = models.BooleanField(blank=True, null=True)
    # image = models.ImageField(blank=True, null=True, upload_to='users/images')

    objects = UserManager()

    USERNAME_FIELD = 'number'