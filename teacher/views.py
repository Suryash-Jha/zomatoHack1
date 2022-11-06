from django.shortcuts import render
from django.http import HttpResponse

def assignmentreport(request):
    return render(request, 'teacher/assignmentreport.html')

def login(request):
    return render(request, 'teacher/login.html')

def signUp(request):
    return render(request, 'teacher/signUp.html')

def assignmentcreator(request):
    return render(request, 'teacher/assignmentcreator.html')





