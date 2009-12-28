from django.conf import settings
from django.contrib.auth.models import User, check_password
from models import Author
from django.db import models
import crypt

class ProfileBackend:
    def authenticate(self, username = None, password = None):
        author = Author.objects.get(name = username)
        if author:
          cryptedpasswd = author.password
          pwd_valid = crypt.crypt(password, cryptedpasswd) == cryptedpasswd
          if pwd_valid:
              try:
                  user = User.objects.get(username = username)
              except User.DoesNotExist:
                  # Create a new user. with the same password as
                  # the author.
                  # Make sure to set password in both models when changed
                  # by user or change this code to store a random
                  # password so that the internal ModelBackend
                  # never succeeds for users who are also MT Authors
                  user = User(username = username, password = password)
                  #user.first_name = author.name
                  #user.first_name = author.name
                  user.is_staff = (author.is_superuser != None)
                  user.is_superuser = (author.is_superuser != None)
                  user.save()
              return user
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk = user_id)
        except User.DoesNotExist:
            return None

class Profile(models.Model): 
    # This is the only required field 
    user = models.ForeignKey(User, unique=True) 
 
    # The rest is completely up to you... 
    author = models.ForeignKey(Author, unique=True) 

