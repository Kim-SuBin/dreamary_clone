# Django가 관리하는 방법

### 3.1 [복습] Hello, Django

- **가상환경이란?**

    자신이 원하는 Python 환경 구축을 위해 필요한 모듈만 담아 놓은 바구니

- **PIP란?**

    Python으로 작성된 패키지 소프트웨어를 관리하는 **패키지 관리 시스템**

- **Project & App**

    여러 개의 App이 모여 Project를 구성

### 3.2 Bootstrap이란?

- Front-End 개발을 빠르고 쉽게 할 수 있는 **오픈 소스 Framework**
- 누구나 쉬운 사용 가능
- 반응형 CSS 제공
- 모든 최신 브라우저와 호환
- PC & 모바일 디자인 제공

### 3.3 URL 관리는 어떻게?

- Django의 URL 관리는 `urls.py` 의 `urlpatterns` 에서 담당
- **Path의 구조**

    ```python
    path('URL', views 내부의 함수, name="url의 이름"),
    ```

    **'URL'** :  페이지 주소 (ex. introduce/, new/)

    **함수** : url이 불렸을 때 실행할 함수 (ex. views.home)

    **name** : 해당 path를 대표하는 이름 (ex. name="home")

    ![path 구조](../img/lecture3(1).png)

### 3.4 Template 언어란?

- Python 변수 & 문법을 HTML에서 쓸 수 있도록 **Django에서 제공하는 언어**

    ![템플릿 언어](../img/lecture3(2).png)

- 템플릿 변수는 결괏값을 나타내기 위해 사용
- 템플릿 태그는 URL을 부르거나, 반복문이나 조건문을 HTML 상에서 수행할 수 있도록 해줌

### 3.5 Static File이란?

- 이미지나 CSS, JS 파일처럼 내용이 고정되어 있어, 응답을 할 때 파일 그대로를 보내주면 되는 파일

    ![static과 media](../img/lecture3(3).png)

### 3.6 Static File 처리하기

1. **Static 폴더 생성**

    App 폴더 내에 static 폴더 만들기 & 파일 생성

2. **Settings&#46;py (Static 설정)**

    ```python
    STATICFILES_DIRS = [
    	os.path.join(BASE_DIR, 'App 이름', 'static')
    ] # Static File들이 들어있는 경로

    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
    # Static File을 모을 디렉토리
    ```

3. **Static 파일 모으기**

    ```bash
    python manage.py collectstatic
    ```

4. **Settings&#46;py (Media 설정)**

    ```python
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

    MEDIA_URL = '/media/'
    ```

5. **urls&#46;py**

    ```python
    from django.conf import settings
    from django.conf.urls.static import static

    urlpatterns=[
    	...
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    ```

6. **HTML에서 사용**

    ```html
    {% load static %}
    ```

### 3.7 Django 프로젝트 실습

**시작 전에 가상환경 키는 것 잊지 말기!! 😉**

1. [부트스트랩 사이트](https://getbootstrap.com/)에 접속
2. Example에 있는 `Album` 클릭

    ![부트스트랩 Example 페이지](../img/lecture3(4).png)

3. 우클릭한 후, 페이지 소스 보기 누르면

    ![Album에서 우클릭](../img/lecture3(5).png)

    소스코드를 볼 수 있어요 🙂

    ![페이지 소스 보기를 누른 결과](../img/lecture3(6).png)

    소스코드를 전체 복사하여 `home.html`에 붙여넣기

    ![home.html에 붙여넣은 모습](../img/lecture3(7).png)

4. BootstrapCDN을 복사하여 `home.html` 에 붙여넣기

    (BootstrapCDN은 외부에 있는 코드나 자원을 가져와서 쓰는 위해 사용)

    ![BootstrapCDN](../img/lecture3(8).png)

    ⬇️ html에 넣을 BootstrapCDN

    ```html
    <!-- CSS only -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">

    <!-- JS, Popper.js, and jQuery -->
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js" integrity="sha384-9/reFTGAW83EW2RDu2S0VKaIzap3H66lZH81PoYlFhbGU+6BZp6G7niu735Sk7lN" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js" integrity="sha384-B4gt1jrGC7Jh4AgTPSdUtOBvfO8shuf57BaghqFfPlYxofvL8/KUEfYiJOMMV+rV" crossorigin="anonymous"></script>
    ```

    `home.html` 에 추가한 모습

    ![home.html에 BootstrapCDN을 추가한 모습](../img/lecture3(9).png)

    `py manage.py runserver` 를 통해 local server를 실행시켜 접속하면 아래와 같은 페이지를 볼 수 있어요 🙂

    ![Django에 부트스트랩 적용한 결과](../img/lecture3(10).png)

5. `home.html` 내용 수정하기!!
    - 데이터베이스에 있는 만큼 카드가 생성되도록 만들기 위해 `home.html` 파일 수정 (`<div class="col-md-4">` 을 하나만 남기고 다 지워주세요)

    ![home.html main 수정](../img/lecture3(11).png)

    - `title` 도 제작하려는 페이지에 맞게 변경

    ![home.html title 변경](../img/lecture3(12).png)

    - `header` 의 샌드위치 박스가 필요하지 않으므로, 내용 삭제

    ![home.html header의 샌드위치 박스 제거](../img/lecture3(13).png)

    - `header` 의  `strong` 부분의 내용 변경

    ![home.html header의 strong 변경](../img/lecture3(14).png)

    - `footer` 내용 수정

    ![home.html footer 수정](../img/lecture3(15).png)

    - `main` 내용 수정

    ![home.html main 수정](../img/lecture3(16).png)

    - 수정된 모습은 다음과 같습니다 🙂

    ![home.html 수정 결과](../img/lecture3(17).png)

6. 소개 페이지를 생성
    - `templates` 에 `introduce.html` 파일을 생성하고 `urls.py` 내용 수정

        ```python
        from django.contrib import admin
        from django.urls import path

        # views.py 파일 연결
        from page import views

        urlpatterns = [
            path('admin/', admin.site.urls),
            path('', views.home, name = "home"),
            path('introduce/', views.introduce, name = "introduce"),
        ]
        ```

    - `views.py` 에 introduce 함수 추가

        ```python
        def introduce(request):
            return render(request, 'introduce.html')
        ```

    - `introduce.html` 에 `home.html`의 내용을 복사하여 붙여 넣고

        title과 main을 다음의 내용으로 변경

        ```html
        <title>Dreamary - 서비스 소개</title>
        ```

        ```html
        <main role="main">
            <div class="jumbotron p-4 p-md-5 text-white rounded bg-dark">
                <div class="col-md-7 px-0">
                    <h1 class="display-4 font-bold">드리머리 - 헤어 서비스 O2O</h1>
                    <p class="lead my-5">
                        "Dreamary"는 헤어샵 예비 헤어 디자이너와 일반 대중을 연결하는 O2O 플랫폼입니다. 플랫폼을 통해 일반 소비자들은 예비 헤어 디자이너들의 이력, 포트폴리오, 리뷰, 별점 등을 확인하고 매우 합리적인 가격에 헤어 서비스를 받을 수 있습니다. "Dreamary"는 지금까지 존재하지 않았던 컨셉의 플랫폼으로, 향후 헤어 시장의 지평에 큰 변화를 가져올 것을 확신합니다.
                    </p>
                </div>
            </div>
        </main>
        ```

    - 수정된 모습은 다음과 같습니다 🙂

        ![introduce 페이지 결과](../img/lecture3(18).png)

7. home 페이지에서 `드리머리 알아보기` 를 누르면 introduce 페이지로 넘어가도록 템플릿 태그 추가

    ```html
    <a href="{% url 'introduce' %}" class="btn btn-outline-danger">드리머리 알아보기</a>
    ```

8. static file들을 저장하기 위해 `page` 폴더 안에 `static` 폴더를 추가하고 그 안에 `css` 와 `images` 폴더 추가
9. static file들을 처리하기 위해 `settings.py` 수정

    ![static 폴더 생성 및 settings.py 수정한 모습](../img/lecture3(19).png)

10. dreamary logo를 `page\static\images` 에 다운받고 static 파일 모으면 static 파일이 생긴 것을 확인 가능

    ![static 파일 모으기 결과](../img/lecture3(20).png)

11. HTML 파일에 맨 위에 `{% load static %}` 를 입력하고 `header` 를 다음과 같이 수정 (home.html과 introduce.html 모두 수정해주세요!!)

    ```html
      <header>
          <div id="navbar" class="navbar navbar-expand-lg navbar-light-bg-light sticky-top">
              <a id="logo" href="{% url 'home' %}" class="navbar-brand align-self-center">
                  <img src="{% static 'images/dreamary_logo.png' %}" width="35" height="35" alt="Dreamary Logo">
                  <label class="navbar-brand align-self-center">Dreamary</label>
              </a>
          </div>
      </header>
    ```

12. CSS 적용을 하기 위해 `page\static\css` 폴더에 `home.css` 와 `introduce.css` 파일을 생성하고 아래 내용 추가

    ```css
    .jumbotron {
        margin-bottom: 0rem;
    }

    label {
        margin-bottom: 0rem;
        font-size: 25px;
    }

    #logo {
        display: flex;
    }

    #navbar {
        display: flex;
        justify-content: space-between;
    }

    footer {
        padding-top: 1.5rem;
    }
    ```

13. `home.html` 에 이미지를 추가했던 방식과 똑같은 방식으로 css 추가

    ```html
    <!-- Custom styles for this template -->
    <link href="album.css" rel="stylesheet">

    <!-- CSS static -->
    <link rel="stylesheet" href="{% static 'css/home.css' %}" />
    ```

    Bootstrap에서 css를 추가하려면 기존의 css 밑에 추가해야 적용이 됩니다!! (css는 순서대로 적용되기 때문입니다 ☺️)

    - 수정된 모습은 다음과 같습니다 🙂

        ![static 적용한 결과](../img/lecture3(21).png)

14. 사용자들이 올린 파일의 URL 관리를 위한 Media 설정
    - `settings.py` 내용 추가

        ```python
        MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

        MEDIA_URL = '/media/'
        ```

    - `urls.py` 내용 변경

        ```python
        from django.conf import settings
        from django.conf.urls.static import static

        urlpatterns = [
            path('admin/', admin.site.urls),
            path('', views.home, name = "home"),
            path('introduce/', views.introduce, name = "introduce"),
        ] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
        ```

**static 파일 모으기는 배포 전에 한 번만 수행해도 괜찮습니다!**

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
