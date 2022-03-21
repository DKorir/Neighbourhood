import email
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager\




class Account(AbstractBaseUser):
    username=models.CharField(max_length=30,unique=True)
    email=models.EmailField(verbose_name="email", max_length=60, unique=True)
    date_joined=models.DateTimeField(verbose_name='date_joined', auto_now_add=True)
    last_login=models.DateTimeField(verbose_name='last_login', auto_now=True)
    is_admin=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username']
    def __str__(self):
        return self.email
    def has_perm(self, perm, obj=None):
        return self.is_admin
    def has_module_perms(self, app_label):
        return True

