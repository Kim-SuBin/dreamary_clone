from django.shortcuts import render, get_object_or_404, redirect

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

def new(request):
    return render(request, 'new.html')

def create(request):
    if request.method == 'POST':
        post = Designer()
        if 'image' in request.FILES:
            post.image = request.FILES['image']
            post.name = request.POST['name']
            post.address = request.POST['address']
            post.description = request.POST['description']

            post.save()

            return redirect('detail', post.id)

def delete(request, designer_id):
    post = get_object_or_404(Designer, pk = designer_id)
    post.delete()

    return redirect('home')