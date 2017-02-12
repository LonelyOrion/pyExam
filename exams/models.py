from __future__ import unicode_literals

from django.db import models
from mongoengine import *
import sys
sys.path.append('..')
from problems.models import Problems
# Create your models here.

connect('pyExam')

class Exams(Document):
	name = StringField(required = True)
	problems = ListField(ReferenceField(Problems))