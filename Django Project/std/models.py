from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _


class Main(models.Model):
    Sno = models.IntegerField(_('Sno'))
    Roll = models.CharField(_('Roll'),max_length=15)
    Name = models.CharField(_('Name'),max_length=20)
    Gender = models.CharField(_('Gender'),max_length=1)
    Cou = models.CharField(_('Cou'),max_length=4)

    def __str__(self):
        return self.Roll


class Group(models.Model):
    Gid = models.IntegerField(_('Sno'))
    Roll = models.CharField(_('Roll'),max_length=15)
    Name = models.CharField(_('Name'),max_length=20)
    Gender = models.CharField(_('Gender'),max_length=1)
    Cou = models.CharField(_('Cou'),max_length=4)

class details(models.Model):
    Roll = models.CharField(_('Roll'),max_length=15)
    Name = models.CharField(_('Name'),max_length=20)
    Gender = models.CharField(_('Gender'),max_length=1)
    Cou = models.CharField(_('Cou'),max_length=4)

class cs_data(models.Model):
    Roll = models.CharField(_('Roll'),max_length=15)
    Name = models.CharField(_('Name'),max_length=20)
    Gender = models.CharField(_('Gender'),max_length=1)
    Cou = models.CharField(_('Cou'),max_length=4)

class ds_data(models.Model):
    Roll = models.CharField(_('Roll'),max_length=15)
    Name = models.CharField(_('Name'),max_length=20)
    Gender = models.CharField(_('Gender'),max_length=1)
    Cou = models.CharField(_('Cou'),max_length=4)
