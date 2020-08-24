# 7. CRUD #1

**📌 CRUD는 Create, Read, Update, Delete의 축약어!**

### 7.1 [복습] Django는 중복을 싫어해

- **URL Include**

    App별로 URL을 관리할 수 있도록 **구조화**

- **Template 상속**

    뼈대가 되는 Base.html을 생성해 **다른 페이지에서 Extends로 불러오기**

### 7.2 GET / POST

- 클라이언트에서 서버로 **요청을 보내는 방법**
- **GET**
    - Data를 "URL"에 포함시켜 전송
    - 전송하는 길이에 제약 O
    - Caching 가능 (REST에서 데이터 조회에 활용)

    ⇒ READ 에서 활용

- **POST**
    - Data를 "Body"에 넣어 전송 (URL에서 노출 X)
    - 전송하는 길이에 제약 X
    - Caching 불가능 (REST에서 데이터 생성에 활용)

    ⇒ CREATE / UPDATE 에서 활용

### 7.3  CREATE

- 새로운 객체를 생성해 **Data를 저장**
- 순서
    1. 객체 생성

        ```python
        if request.method == 'POST':
            post = Designer()
        ```

    2. 입력 Data 저장

        ```python
        post.name = request.POST['name']
        post.address = request.POST['address'] ...
        ```

        ```python
        post.save()
        ```

### 7.5 UPDATE

- 정보 수정이 필요한 객체를 찾아 **Data를 새롭게 저장**
- 순서
    1. 객체 탐색

        ```python
        post = get_object_or_404(Designer, pk = designer_id)

        if request.method == 'POST':
        ```

    2. 입력 Data 저장

        ```python
        post.name = request.POST['name']
        post.address = request.POST['address'] ...
        ```

        ```python
        post.save()
        ```

### 7.6 DELETE

- 제거가 필요한 객체를 찾아 **삭제**
- 순서
    1. 객체 탐색

        ```python
        post = get_object_or_404(Designer, pk = designer_id)
        ```

    2. 객체 삭제

        ```python
        post.delete()
        ```

    3. Home으로 이동

        ```python
        return redirect('home')
        ```

### 7.7 Django 프로젝트 실습하기

**시작 전에 가상환경 키는 것 잊지 말기!! 😉**

1. admin이 아닌 홈페이지에서 디자이너를 추가할 수 있도록 `new.html` 과 `new.css` 를 만들어줍니다.

    👉 [new.html 보러가기](https://gist.github.com/Kim-SuBin/ae71af9c255a6e4599191733f3e8ee83)

2. `new.html` 을 보기 위해 `urls.py` 에 new path를 추가하고, `views.py` 에 new 함수를 추가합니다.
    - urls&#46;py

    ```python
    from django.urls import path
    from . import views

    urlpatterns = [
        path('', views.home, name = "home"),
        path('introduce/', views.introduce, name = "introduce"),
        path('profile/<int:designer_id>/', views.detail, name = "detail"),
        # 추가한 path
        path('new/', views.new, name = "new"),
    ]
    ```

    - views&#46;py

        ```python
        def new(request):
            return render(request, 'new.html')
        ```

3. 등록하기 버튼 생성을 위해 `base.html` 을 수정합니다.

    👉 [base.html 보러가기](https://gist.github.com/Kim-SuBin/e3796c306da3ec2aae0a542d429e2eef)

4. `create` 적용하기 위해 `urls.py` 에 create path를 추가하고,  `views.py` 에 create 함수를 추가합니다. 
    - urls&#46;py

        ```python
        from django.urls import path
        from . import views

        urlpatterns = [
            path('', views.home, name = "home"),
            path('introduce/', views.introduce, name = "introduce"),
            path('profile/<int:designer_id>/', views.detail, name = "detail"),
            path('new/', views.new, name = "new"),
            # 추가한 path
            path('create/', views.create, name="create"),
        ]
        ```

    - views&#46;py

        ```python
        # import에 redirect를 추가해줘야해요!!
        from django.shortcuts import render, get_object_or_404, redirect

        def create(request):
            if request.method == 'POST':
                post = Designer()
                if 'image' in request.FILES:
                    post.image = request.FILES['image']
                    post.name = request.POST['name']
                    post.address = request.POST['address']
                    post.description = request.POST['description']

                    post.save()

                    # redirect는 주소로 이동하는 느낌!
                    return redirect('detail', post.id)
        ```

5. create를 만들어봤으니 이번에는 `delete` 를 만들어볼까요?! 우선 delete를 적용시키기 위해 `detail.html` 에 다음 내용을 추가해줘야해요.

    ```html
    <a href="{% url 'delete' designer.id %}" class="btn btn-sm btn-outline-danger">정보 삭제</a>
    ```

    👉 [detail.html 보러가기](https://gist.github.com/Kim-SuBin/7db4bfb18f8c0c7cb7f1702e1e250c41)

6. `delete` 를 적용하기 위해 `urls.py` 에 delete path를 추가하고, `views.py]` 에 delete 함수를 추가합니다.
    - urls&#46;py

    ```python
    path('delete/<int:designer_id>/', views.delete, name="delete"),
    ```

    - views&#46;py

    ```python
    def delete(request, designer_id):
        post = get_object_or_404(Designer, pk = designer_id)
        post.delete()

        return redirect('home')
    ```

7. local server를 실행시켜 확인해볼까요? 🙂

    웹페이지의 버튼을 누른 후

    ![디자이너 등록하기 버튼 클릭](../img/lecture7(1).png)

    내용을 작성하고 디자이너를 등록해봅시다.

    ![디자이너에 관한 정보 입력](../img/lecture7(2).png)

    등록하면 다음과 같은 페이지가 뜹니다 😉

    ![등록된 모습 (디테일 페이지)](../img/lecture7(3).png)

    admin에도 강아지 친구에 대한 정보가 추가되었네요 ☺️

    ![새로운 디자이너가 추가된 amdin](../img/lecture7(4).png)

    드리머리에 새로운 디자이너 선생님이 오셨네요 🐶

    ![드리머리 사이트 재접속하면 새로운 디자이너가 추가됨](../img/lecture7(5).png)

    이제 삭제도 잘되는지 확인해볼까요?

    ![강아지 디자이너 삭제](../img/lecture7(6).png)

    삭제를 누르고 나면 아래와 같이 사라진 것을 확인할 수 있습니다. (강아지 선생님 안녕 👋)

    ![삭제된 모습이 반영된 드리머리 홈페이지](../img/lecture7(7).png)

    admin에서도 사라졌네요 😢

    ![admin에서도 삭제 확인](../img/lecture7(8).png)


<br />

---

### 📝 강의
1. [Django,  그게 뭐야???](./lecture_1.md)
2. [Hello, Django](./lecture_2.md)
3. [Django가 관리하는 법](./lecture_3.md)
4. [Django로 나를 소개해볼게 #1](./lecture_4.md)
5. [Django로 나를 소개해볼게 #2](./lecture_5.md)
6. [Django는 중복을 싫어해](./lecture_6.md)
7. [CRUD #1](./lecture_7.md)
8. [CRUD #2](./lecture_8.md)