# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class ContactEntry(models.Model):
    subject = models.CharField(max_length=100)
    text = models.TextField()
    
    def __unicode__(self):
        return self.subject