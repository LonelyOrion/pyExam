#coding: utf-8
from django.shortcuts import render
from django.http import HttpResponseRedirect
from models import Problems
from utils import IDGenerator

# Create your views here.

def showProblems(request):
	nickname = request.session['nickname']
	problems = Problems.objects()
	return render(request, 'showProblems.html', locals())

def addProblem(request):
	return render(request, 'addProblem.html')
def addProblems(request):
	return render(request, 'addProblems.html')

def addProblemCheck(request):
	try:
		rawProblem = request.POST['problem'].strip('\r\n')
		rawOptions = request.POST['options'].split('\r\n')
		rawAnswer = request.POST['answer'].strip('\r\n')
		rawType = request.POST['type']
	except:
		return render(request, 'info.html', {'info': '提交内容不完整', 'link': '/showProblems/'})

	myID = IDGenerator().getRandomID()
	problem = Problems(myID = myID, problem = rawProblem, options = rawOptions, answer = rawAnswer, type = rawType)
	problem.save()

	return HttpResponseRedirect('/showProblems/')

def addProblemsCheck(request):
	try:
		problems = request.POST['problems']
		rawType = request.POST['type']
	except:
		return render(request, 'info.html', {'info': '提交内容不完整', 'link': '/showProblems/'})

	problems = problems.split('\r\n\r\n')	#warning: this may be different in different browsers
	for problem in problems:
		arr = problem.split('\r\n')
		rawProblem = arr[0]
		rawAnswer = arr[-1]
		rawOptions = arr[1: -1]

		myID = IDGenerator().getRandomID()
		newProblem = Problems(myID = myID, problem = rawProblem, options = rawOptions, answer = rawAnswer, type = rawType)
		newProblem.save()
	return HttpResponseRedirect('/showProblems/')

def editProblem(request):
	try:
		myID = request.GET['myID']
	except:
		return render(request, 'info.html', {'info': '错误的请求方式', 'link': '/showProblems/'})
	problem = Problems.objects(myID = myID)
	if len(problem) == 0:
		return render(request, 'info.html', {'info': '错误的请求ID', 'link': '/showProblems/'})

	problem = problem[0]
	problem.options = '\n'.join(problem.options)
	print problem.options
	return render(request, 'editProblem.html', {'problem': problem})

def editProblemCheck(request):
	try:
		rawProblem = request.POST['problem']
		rawOptions = request.POST['options']
		rawAnswer = request.POST['answer']
		myID = request.POST['myID']
		rawType = request.POST['type']
	except:
		return render(request, 'info.html', {'info': '提交内容不完整', 'link':'/showProblems/'})

	problem = Problems.objects(myID = myID)
	if len(problem) == 0:
		return render(request, 'info.html', {'info': '错误的请求ID', 'link':'/showProblems/'})

	problem = problem[0]
	problem.problem = rawProblem.strip('\r\n')
	problem.options = rawOptions.split('\r\n')
	problem.answer = rawAnswer
	problem.type = rawType
	problem.save()

	return HttpResponseRedirect('/showProblems/')

def deleteProblem(request):
	try:
		myID = request.GET['myID']
	except:
		return render(request, 'info.html', {'info': '错误的请求方式', 'link':'/showProblems/'})

	problem = Problems.objects(myID = myID)
	if len(problem) == 0:
		return render(request, 'info.html', {'info': '错误的请求ID', 'link':'/showProblems/'})

	problem = problem[0]
	problem.delete()
	return HttpResponseRedirect('/showProblems/')