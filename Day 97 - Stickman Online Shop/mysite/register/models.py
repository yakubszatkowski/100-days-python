from django.db import models
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser


class AppUserManager(BaseUserManager):

    def create_user(self, username, email, password=None):
        if not username:
            raise ValueError('A username is required')
        if not email:
            raise ValueError('An email is required')
        if not password:
            raise ValueError('A password is required')
        
        user = self.model(
            email=self.normalize_email(email),
            username=username
        )
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, email, password=None):
        if not username:
            raise ValueError('A username is required')
        if not email:
            raise ValueError('An email is required')
        if not password:
            raise ValueError('A password is required')
        
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True 
        user.save()

        return user


class AppUser(AbstractBaseUser):
    # Uniques
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=50, unique=True)

    # Necessaries
    date_joined = models.DateTimeField (verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField (verbose_name='last login', auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    objects = AppUserManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True
