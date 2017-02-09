from django.shortcuts import render_to_response
from django.http import HttpResponse

# Create your views here.
def login(request):
	return render_to_response('login.html',  {'userName': 'jayz'})

def loginCheck(request):
	return render_to_response('loginCheck.html')