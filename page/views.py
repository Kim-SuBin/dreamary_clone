from django.shortcuts import render, get_object_or_404

# Create your views here.

# Model의 존재 알려주기
from .models import Designer

#Q= Querset을 Templates로 보내기
def home(request):
    # Designer.objects.all()는 method!
    designers = Designer.objects.all()
    return render(request, 'home.html', {'designers':designers})

def introduce(request):
    return render(request, 'introduce.html')

# pk로 designer_id를 받아옵니다.
def detail(request, designer_id):
    designer = get_object_or_404(Designer, pk = designer_id)
    return render(request, 'detail.html', {'designer' : designer})