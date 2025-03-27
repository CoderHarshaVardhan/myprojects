from django.contrib.auth.models import User
from django.db.models.signals import post_save
from alert.utils import BaseAlert

class WelcomeAlert(BaseAlert):
    title = 'Welcome new users'
    description = 'When a new user signs up, send them a welcome email'

signal = post_save
sender = User

default = False

def before(self, created, **kwargs):
    return created

def get_applicable_users(self, instance, **kwargs):
    return [instance]