from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def login(request):
	return render(request, 'login.html',  {'userName': 'jayz'})

def loginCheck(request):
	if request.POST.has_key('username'):
		username = request.POST['username']
	else:
		print 'no'
	if request.POST.has_key('password'):
		password = request.POST['password']
	else:
		print 'no'
	return render(request, 'loginCheck.html')