from django.shortcuts import render

# Create your views here.

def home(request):
    # request가 들어오는 경우 home.html을 return
    return render(request, 'home.html')