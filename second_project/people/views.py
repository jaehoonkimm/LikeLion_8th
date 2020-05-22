from django.shortcuts import render
from .models import Person

# Create your views here.
def home(request):
    person = Person.objects #Person 안의 모든 objects를 가져온다. (queryset 쿼리셋)
    return render(request, 'home.html', {'persons':person})