from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def login(request):
	return render(request, 'login.html',  {'userName': 'jayz'})

def loginCheck(request):
	return render(request, 'loginCheck.html')