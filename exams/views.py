import sys
from django.shortcuts import render
sys.path.append('..')
from problems.models import Problems

# Create your views here.

def showExams(request):
	nickname = request.session['nickname']
	return render(request, 'showExams.html', locals())

def addExam(request):
	singles = Problems.objects(type='single')
	multiples = Problems.objects(type='multiple')
	corrections = Problems.objects(type='correction')
	return render(request, 'addExam.html', locals())
