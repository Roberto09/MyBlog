from django.shortcuts import render, render_to_response

# Create your views here.

def HomeScreen(request):
	return render_to_response('index.html')

def AboutMe(request):
	return render_to_response('aboutme/aboutme.html')

def Academic(request):
	return render_to_response('academic/academic.html')
