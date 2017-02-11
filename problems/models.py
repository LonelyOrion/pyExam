from __future__ import unicode_literals

from django.db import models
from mongoengine import *

# Create your models here.

connect('pyExam')

class Problems(Document):
	problem = StringField()
	options = ListField(StringField(), default=list)
	answer = StringField()