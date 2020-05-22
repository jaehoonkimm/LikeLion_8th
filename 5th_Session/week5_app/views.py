from django.shortcuts import render
from .models import youtube

def home(request):
    channels = youtube.objects
    return render(request, 'home.html', {'channels':channels})
