# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Account(models.Model):
    STOP_OR_NOT_CHOICES = (
        (0, 'ACTIVE'),
         (1, 'STOPPED')
         )
    account_id = models.CharField(max_length=64, )
    phonenumber = models.CharField(max_length=11, )
    email = models.CharField(max_length=60)
    account_type = models.CharField(max_length=30)
    created_time = models.DateTimeField()
    last_modified_time = models.DateTimeField()
    stop = models.SmallIntegerField(choices=STOP_OR_NOT_CHOICES, default=0)

class VerifyInfo(models.Model):
    
    account = models.OneToOneField(
        Account, 
        on_delete=models.CASCADE, 
        primary_key=True,)
    verifymsg = models.CharField(max_length=200)
    valid_time = models.DateTimeField()
    created_time = models.DateTimeField()
    verify_type = models.CharField(max_length=30)
    