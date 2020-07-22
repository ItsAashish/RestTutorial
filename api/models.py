from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from  django.contrib.auth.models import BaseUserManager
from django.conf import settings
# Create your models here.


class Todo(models.Model):
    """" The basic Todo Model """
    author = models.CharField(max_length = 50, null = True, blank = True)
    name = models.CharField(max_length = 50 , blank = True, null = True)
    description = models.CharField(max_length = 500 , blank = True, null = True)
    completed = models.BooleanField(default = False, blank = False, null = False)


    def __str__(self):
        return self.name


class UserProfileManager(BaseUserManager):
    """ Manager for User Profile Below """
    def create_user(self, name, email, password = None):
        if not email:
            raise ValueError("Users Must have an email Address.")
        email = self.normalize_email(email)
        if not name:
            raise ValueError("Users Must have an Name.")

        # create a user model instance / creating a user
        user = self.model(email = email, name = name)
        user.set_password(password)
        user.save(using = self._db)
        return user


    def create_superuser(self,email,name,password):
        """  create a superuser """
        user = self.create_user(name, email, password)
        user.is_superuser   = True
        user.is_staff       = True
        # is_admin isn't the part of the UserProfile Model
        # user.is_admin       = True
        user.save(using = self._db)




class UserProfile(AbstractBaseUser, PermissionsMixin):
    """   Represents a user profile """
    email = models.EmailField(max_length = 60 , unique = True)
    name = models.CharField(max_length = 100)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)

    objects = UserProfileManager()
# tHE USERNAME FIELD IS FOR DETERMINING WHETHER WE USE EMAIL USERNAME OR ANYTHING AS THE LOGIN VALUE
    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """ gets the Full Name  Value """
        return f'{self.name}'
    
    def get_short_name(self):
        """ gets the Short Name Value"""
        return f'{self.name}'

    def __str__(self):
        """ This returns the String That is shown in the Tabular form """
        return f'{self.email}'
    

class ProfileFeed(models.Model):
    """ Profile status update """
    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE

    )
    status_text = models.CharField(max_length = 255)
    date_created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f'{self.status_text}'