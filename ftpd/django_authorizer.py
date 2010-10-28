import os
import sys

from django.conf import settings
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate

from pyftpdlib.ftpserver import DummyAuthorizer

class DjangoAuthorizer(DummyAuthorizer):
    """Django Authorizer"""
    
    def __init__(self):
        self.user_perms = "elradfmw"

    def add_user(self, username, password, homedir, perm='elr',
                    msg_login="Login successful.", msg_quit="Goodbye."):
        raise Error("Not allowed")

    def add_anonymous(self, homedir, **kwargs):
        raise Error("Not allowed")

    def remove_user(self, username):
        raise Error("Not allowed")

    def validate_authentication(self, username, password):
        """Return True if the supplied username and password match the
        stored credentials."""
        return authenticate(username=username, password=password) != None


    def has_user(self, username):
        """Whether the username exists in the virtual users table."""
        try:
           User.objects.get(username=username)
           return True
        except Error, e:
           return False

    def in_user_dir(self, username, path):
        norm_path = os.path.normcase(path)
        return self._issubpath(norm_path, self.get_home_dir(username))

    def has_perm(self, username, perm, path=None):
        """Whether the user has permission over path (an absolute
        pathname of a file or a directory).

        Expected perm argument is one of the following letters:
        "elradfmw".
        """
        if path is None or self.in_user_dir(username, path):
            return perm in self.user_perms
        else:
            return False

    def get_perms(self, username):
        """Return current user permissions."""
        return self.user_perms

    def get_home_dir(self, username):
        """Return the user's home directory."""
        return os.path.normcase(os.path.join(settings.FTP_BASE, username))

    def get_msg_login(self, username):
        """Return the user's login message."""
        return "Welcome"

    def get_msg_quit(self, username):
        """Return the user's quitting message."""
        return "Bye"

    def _issubpath(self, a, b):
        """Return True if a is a sub-path of b or if the paths are equal."""
        p1 = a.rstrip(os.sep).split(os.sep)
        p2 = b.rstrip(os.sep).split(os.sep)
        return p1[:len(p2)] == p2
