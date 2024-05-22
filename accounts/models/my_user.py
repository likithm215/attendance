from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.contrib.auth.models import BaseUserManager, AbstractUser, _user_has_perm, _user_has_module_perms, Permission, Group



class MyUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        """
        Creates and saves a regular User with the given username, email and password.
        """
        extra_fields.setdefault('is_student', True)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email, password=None, **extra_fields):
        """
        Creates and saves a superuser with the given username, email and password.
        """
        extra_fields.setdefault('is_student', False)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self._create_user(username, email, password, **extra_fields)

    def _create_user(self, username, email, password, **extra_fields):
        """
        Creates and saves a User with the given username, email and password.
        """
        if not username:
            raise ValueError('The given username must be set')
        if not email:
            raise ValueError('The given email must be set')
        
        email = self.normalize_email(email)
        now = timezone.now()
        user = self.model(
            username=username,
            email=email,
            last_login=now,
            date_joined=now,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    

import uuid

class MyUser(AbstractUser):
    groups = models.ManyToManyField(
        Group,
        related_name='myuser_set', 
        blank=True,
        help_text=('The groups this user belongs to. A user will get all permissions granted to each of their groups.'),
        related_query_name='myuser',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='myuser_set', 
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='myuser',
    )
    # User Profile
    id = models.CharField(max_length=36, primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(_('user_field_username'), max_length=30, unique=True, help_text=_('user_field_usernameHelpTxt'))
    password = models.CharField(_('user_field_password'), max_length=128, editable=True)
    first_name = models.CharField(_('user_field_firstName'), max_length=30, blank=True)
    last_name = models.CharField(_('user_field_lastName'), max_length=30, blank=True)
    email = models.EmailField(_('user_field_email'), blank=True)
    login_id = models.IntegerField(null=True, blank=True, default=0)
    login_type = models.IntegerField(null=True, blank=True, default=0)
    is_student = models.BooleanField(_('user_field_staff'), default=False, help_text=_('user_field_staffStatusHelpTxt'))
    date_joined = models.DateTimeField(_('user_field_dateJoined'), default=timezone.now)
    last_login = models.DateTimeField(_('user_field_lastLogin'), blank=True, null=True)
    mobile = models.CharField(max_length=20, null=True, blank=True)
    college_name = models.CharField(_('user_field_current_company'), max_length=36, null=True, blank=True)
    objects = MyUserManager()
