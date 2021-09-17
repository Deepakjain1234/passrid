from django.db import models

from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import RegexValidator

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user


# User Registration Model
class User(AbstractBaseUser, PermissionsMixin):

    id = models.BigAutoField(primary_key=True, db_index=True)
    email = models.EmailField(verbose_name='Email',
                              max_length=255, unique=True)
    is_passituser = models.BooleanField(default=False)
    is_websiteowner = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    is_active = models.BooleanField(default=True)
    admin = models.BooleanField(default=False)
    staff = models.BooleanField(default=False)


    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def __unicode__(self):
        return self.email

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_superuser(self):
        "Is the user a admin member?"
        return self.admin

    objects = UserManager()


class PassitUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phone_number = models.CharField(max_length=10, unique=True, validators=[
                                    RegexValidator(r'^\d{1,10}$')], blank=False, default="", verbose_name='Phone No.')
    name = models.CharField(max_length=64, default="", blank=False)

    USERNAME_FIELD = ['name']

    def __str__(self):
        return self.name


class WebsiteOwner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    wuid = models.BigAutoField(primary_key=True, db_index= True)
    phone_number = models.CharField(max_length=10, unique=True, validators=[
                                    RegexValidator(r'^\d{1,10}$')], blank=True, default="", verbose_name='Phone No.')
    owner_name = models.CharField(max_length=64, default="", blank=False)
    domain = models.URLField(max_length=64, unique=True, blank=False, verbose_name='Website')

    USERNAME_FIELD = ['domain']

    def __str__(self):
        return self.domain
