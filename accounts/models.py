from django.db import models

from django.contrib.auth.models import AbstractUser


from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

class User(AbstractUser):
    ROLES = (
        ('AD', 'Admin'),
        ('CL', 'Client'),
        ('ST', 'Staff'),
        ('MG', 'Manager'),
        ('SE', 'Sales Executive')

    )

    CATERGORIES = (
        ('SAE', 'Salary Earner'),
        ('BO', 'Business Owner'),
        ('CO', 'Corper')
    )
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    role = models.CharField(max_length=30, choices = ROLES, blank=True)
    category = models.CharField(max_length=50, choices = CATERGORIES, blank=True)
# Create your models here.

class Register(models.Model):

    title = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    email = models.EmailField()
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=300)
    phone = models.CharField(max_length=15)
    status = models.CharField(max_length=100)
    dob = models.CharField(max_length=100)
    identification = models.CharField(max_length=500)
    category = models.CharField(max_length=200)
    username = models.CharField(max_length=100)
    password1 = models.CharField(max_length=100)
    password2 = models.CharField(max_length=100)
    checkbox = models.BooleanField(default=False)
    #is_verified = models.BooleanField(default=False)

class user_create(models.Model):

    title = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    email = models.EmailField()
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=300)
    phone = models.CharField(max_length=15)
    status = models.CharField(max_length=100)
    birth_date = models.CharField(max_length=100)
    identification = models.CharField(max_length=500)
    category = models.CharField(max_length=200)
    username = models.CharField(max_length=100)
    password1 = models.CharField(max_length=100)
    password2 = models.CharField(max_length=100)
    role = models.CharField(max_length=10)
    note = models.TextField()
    #is_verified = models.BooleanField(default=False)


