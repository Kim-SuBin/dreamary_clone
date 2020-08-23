## 6. Django는 중복을 싫어해

### 6.1 [복습] Django로 나를 소개해볼게 #2

- **Queryset & Method**

    전달받은 객체 목록, 그리고 이를 다루는 법

- **PK (Primary Key)**

    Model을 통해 생성된 객체들을 구분할 수 있는 **"고유한" Key**

- **Path Convertor**

    여러 객체의 url을 **"계층적으로" 다룰 수 있도록 도와주는 도구**

- **get_object_or_404**

    객체를 가져오려 했는데 **없을 경우 나타나는 에러**

### 6.2 URL Include

- App 별로 URL을 관리할 수 있도록 구조화
- 각각의 App의 url이 Project에서 관리하면 복잡해지므로

    ![url 분리 전](../img/lecture6(1).png)

    각각의 App에 `urls.py` 를 생성하여 체계적으로 관리

    ![url 분리 후](../img/lecture6(2).png)

- App 폴더 내에 `urls.py` 생성 후, 아래와 같이 입력

    ```python
    from django.urls import path
    from . import views

    urlpatterns = [
    ]
    ```

- Project 폴더 내의 `urls.py` 는 다음과 같이 수정

    ```python
    from django.urls import path, include

    urlpatterns = [
        path('url/', include('app이름.urls'),
    ]
    ```

### 6.3 Template 상속

**시작 전에 가상환경 키는 것 잊지 말기!! 😉**

- 중복 코드를 `base.html` 에서 관리

    ![base.html](../img/lecture6(3).png)

- 코드를 수정할 때 다음과 같은 느낌으로!

    ![base.html로 코드 리팩토링 하는 법](../img/lecture6(4).png)

### 6.4 Django 프로젝트 실습


1. `page` App 폴더 내에 `urls.py` 생성 후, 다음과 같이 내용을 추가해줍니다.

    ```python
    from django.urls import path
    from . import views

    urlpatterns = [
        path('', views.home, name = "home"),
        path('introduce/', views.introduce, name = "introduce"),
        path('profile/<int:designer_id>/', views.detail, name = "detail"),
    ]
    ```

2. `dreamaryproject` 폴더 내에 `urls.py` 는 다음과 같이 수정합니다.

    ```python
    from django.contrib import admin
    # include 추가 필수!!!
    from django.urls import path, include
    from page import views
    from django.conf import settings
    from django.conf.urls.static import static

    urlpatterns = [
        path('admin/', admin.site.urls),
        # project는 app으로 연결하는 역할만 수행
        path('', include('page.urls')),
    ] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    ```

3. `templates` 폴더 내에 `base.html` 파일을 생성하고 다음과 같이 입력해주세요.

    (구조적으로는 project에 넣는 것이 맞지만 app 안에 만들어도 상관없어요 🙂)

    👉 [base.html 코드 보러가기](https://gist.github.com/Kim-SuBin/8df0be8091fd508db37d0312170b963b)

    `home.html` 과 `introduce.html` 에서 `base.html` 과 중복되는 부분을 제거하고 형식에 맞춰 내용을 수정해주세요.

    👉 [home.html 코드 보러가기](https://gist.github.com/Kim-SuBin/fab742127ed221af88db6dfc1d5553d5)

    👉 [introduce.html 코드 보러가기](https://gist.github.com/Kim-SuBin/6bf49a37a63b808efa164a02a3816446)

    `base.html` 에서 사용할 `base.css` 를 `static\css` 에 추가하고 다음과 같이 입력해주세요.

    ```css
    label {margin-bottom: 0rem; font-size: 25px;}

    #logo {display: flex;}

    #navbar {display: flex; justify-content: space-between;}

    footer {padding-top: 1.5rem;}
    ```

    `home.css` 와 `introduce.css` 에서 `base.css` 와 중복되는 부분을 제거하여 다음과 같이 수정해주세요.

    ```css
    .jumbotron {margin-bottom: 0rem;}
    ```

📌 Templates 상속과 같은 작업을 **코드 리팩토링**이라고 해요! <br />
다소 귀찮게 느껴질수도 있지만, 변경사항이 생겼을 때 도움이 되니까 이 작업을 해주는 게 좋아요 😆


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