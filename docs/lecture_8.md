# 8. CRUD #2

### 8.1 [복습] CRUD #1

- **CRUD**

    CREATE / READ / UPDATE / DELETE

- **GET / POST**

    클라이언트에서 서버로 **요청을 보내는 방법**

### 8.2 UPDATE

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

### 8.3 패키지 종속성 관리

- 내 환경에서 어떤 패키지들 어떤 버전으로 사용하고 있는지 알려주는 것

    ![패키지 종속성 관리 방법](../img/lecture8(1).png)

- `패키지 설치`는 다른 사람들이 정의해놓은 패키지를 설치하는 방법에 대한 내용이고, `패키지 정의`는 추가로 패키지를 설치했을 때 다른 사람들이 그 패키지를 설치할 때 반영되도록 하는 방법

### 8.4 Django 프로젝트 실습하기

시작 전에 가상환경 키는 것 잊지 말기!! 😉

1. 디자이너의 정보를 수정할 수 있도록 `update.html` 과 `update.css` 를 만들어줍니다.

    👉 [update.html 보러가기](https://gist.github.com/Kim-SuBin/9569c551f6b587096b95358cf9227a0d)

2. `new.html` 을 보기 위해 `urls.py` 에 new path를 추가하고, `views.py` 에 new 함수를 추가합니다.
    - urls&#46;py

        ```python
        path('update/<int:designer_id>/', views.update, name="update"),
        ```

    - views&#46;py

        ```python
        def update(request, designer_id):
            post = get_object_or_404(Designer, pk = designer_id)
            
            if request.method == 'POST':
                if 'image' in request.FILES:
                    post.image = request.FILES['image']
                post.name = request.POST['name']
                post.address = request.POST['address']
                post.description = request.POST['description']

                post.save()

                return redirect('detail', post.id)
            else:
                return render(request, 'update.html', {'designer' : post})
        ```

3. 내용이 수정되는지 확인해볼까요?

    앨리스 정원에서 활동 중인 토끼 디자이너 선생님이 다른 곳으로 가셨다고 하네요 🙀

    ![정보 수정을 위해 자세히 알아보기 클릭](../img/lecture8(2).png)

    정보를 수정해볼까요?

    ![디테일 페이지에서 정보 수정 클릭](../img/lecture8(3).png)

    address의 내용을 수정하고, 수정 완료하기 버튼을 누르면

    ![내용 변경 후 수정 완료하기 클릭](../img/lecture8(4).png)

    토끼 디자이너 선생님의 활동 위치가 바뀐 것을 확인 할 수 있습니다.

    ![디테일 페이지에서 변경된 내용 확인](../img/lecture8(5).png)

    홈페이지에도 바뀐 정보가 들어가있네요. 🐰

    ![드리머리 홈페이지에서 변경된 내용 확인](../img/lecture8(6).png)

4. 마지막으로 패키지 정의를 해봅시다.

    ```bash
    pip freeze > requirements.txt
    ```

    명령어를 입력하면 다음과 같이 `requirements.txt` 파일이 생성된 것을 확인 할 수 있어요!

    ![패키지 정의 후 생성된 파일](../img/lecture8(7).png)


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