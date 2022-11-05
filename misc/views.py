from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'misc/homePage.html')

def courses(request):       
    return render(request, 'courses.html')

def feed(request):
    return render(request, 'feed.html')

def leaderacad(request):
    return render(request, 'leaderboardAcademics.html')

def leadercocurr(request):
    return render(request, 'leaderboardCocurricular.html')



