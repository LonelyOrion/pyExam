import sys
from django.shortcuts import render
from django.http import HttpResponseRedirect
from models import Exams
sys.path.append('..')
from problems.models import Problems

# Create your views here.

def showExams(request):
	nickname = request.session['nickname']
	exams = Exams.objects().all()
	return render(request, 'showExams.html', locals())

def addExam(request):
	singles = Problems.objects(type='single')
	multiples = Problems.objects(type='multiple')
	corrections = Problems.objects(type='correction')
	return render(request, 'addExam.html', locals())

def addExamCheck(request):
	exam = Exams(name="test")

	singles = Problems.objects(type='single')
	for single in singles:
		if request.POST[single.myID] == 'true':
			exam.problems.append(single)
	exam.save()
	#multiples = Problems.objects(type='multiple')
	#corrections = Problems.objects(type='correction')
	return HttpResponseRedirect('/showExams/')
