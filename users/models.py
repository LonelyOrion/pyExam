from __future__ import unicode_literals

from django.db import models
from mongoengine import *
# Create your models here.

connect('pyExam')

class Users(Document):
	username = StringField(max_length = 30, required = True)
	password = StringField(max_length = 30, required = True)
	nickname = StringField(max_length = 30, required = True)