import os

from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.conf import settings

def create_user_dir(sender, **kwargs):
    username = kwargs['instance'].username
    home_dir = os.path.join(settings.FTP_BASE, username)
    os.mkdir(home_dir)

post_save.connect(create_user_dir,sender=User)
