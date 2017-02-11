#coding: utf-8
from django.shortcuts import render
from models import Problems

# Create your views here.

def showProblems(request):
	nickname = request.session['nickname']
	problems = Problems.objects()
	
	return render(request, 'showProblems.html', locals())

def addProblems(request):
	return render(request, 'addProblems.html')

def addProblemsCheck(request):
	try:
		rawProblem = request.POST['problem']
		rawOptions = request.POST['options']
		rawAnswer = request.POST['answer']
	except:
		return render(request, 'info.html', {'info': '提交内容不完整'})

	problem = rawProblem.strip('\r\n')
	options = rawOptions.split('\n')
	answer = rawAnswer.strip('\r\n')
	problem = Problems(problem = problem, options = options, answer = answer)
	problem.save()

	return render(request, 'showProblems.html')