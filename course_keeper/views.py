from django.shortcuts import render

#play a game

#create a course

# Create your views here.
def scorecard(request):
    
    return render(request, 'scorecard.html', context={})

def home(request):
    return render(request, 'home.html', context={})

