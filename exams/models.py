from __future__ import unicode_literals

from django.db import models
from mongoengine import *
# Create your models here.

connect('pyExam')

class Exams(Document):
	name = StringField(required = True)