from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from .utils import normalize_email


# Custom User Manager
class UserManager(BaseUserManager):
    def create_user(self, email, name, username, password=None, password2=None):
        user = self.model(
            email=normalize_email(email),
            email2=email.strip(),
            username=username.strip().lower(),
            username2=username.strip(),
            name=name.strip()
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, username, password=None):
        user = self.create_user(
            email=email,
            username=username,
            name=name,
            password=password,
        )
        user.is_admin = True
        user.is_premium = True
        user.save(using=self._db) 
        return user

# Custom User Model
class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="Email",
        max_length=255,
        unique=True,
    )
    email2 = models.EmailField(
        verbose_name="Original Email",
        max_length=255,
        unique=True,
    )
    name = models.CharField(
        verbose_name="Name",
        max_length=200,
    )
    username = models.CharField(
        verbose_name="Username",
        max_length=150,
        unique=True,
    )
    username2 = models.CharField(
        verbose_name="Original Username",
        max_length=150,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    is_premium = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    objects = UserManager()
    

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name", "username"]

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin