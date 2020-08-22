# 2. Hello, Django

### 2.1 [복습] Django, 그게 뭐야?

- **Django 란?**

    Python으로 작성된 오픈 소스 웹 어플리케이션 프레임워크

- **Framework 란?**

    기본적으로 필요한 기능을 갖춰, 원하는 기능 구현에 집중하도록 도와주는 개발 환경

- **MTV  패턴이란?**

    Model - View - Template

### 2.2 가상환경

- 자신이 원하는 Python 환경 구축을 위해 필요한 모듈만 담아놓은 **바구니**

    ![가상환경](../img/lecture2(1).png)

### 2.3 PIP 란?

- Python으로 작성된 패키지 소프트웨어를 관리하는 **패키지 관리 시스템**

    ![PIP](../img/lecture2(2).png)

### 2.4 단축키/명령어 모음

1. VS Code 단축키 모음
    - **[터미널 생성]** Ctrl + Shift + ` (키보드에서 ~ 찾기)
    - **[터미널에서 이전에 썼던 명령어 불러오기]** 터미널에서 ↑ 키 누르기
    - **[현재 커서 위치의 코드 복사]** Ctrl + D (여러 줄 복사도 가능)
    - **[현재 커서 위치의 코드 이동]** Alt + ↑ or ↓
2. 가상환경 명령어 모음
    - **[가상환경 생성]** python -m venv <가상환경 이름>
    - **[가상환경 활성화 (윈도우)]** source <가상환경 이름>/Scripts/activate
    - **[가상환경 끄기]** deactivate
3. Django 명령어 모음
    - **[Django 패키지 설치]** pip install django
    - **[Django 프로젝트 생성]** django-admin startproject <프로젝트명> .

        (마지막에 .(온점)붙이면 새로운 폴더가 생기지 않습니다.)

    - **[Django App 생성]** python manage&#46;py startapp <App 이름>
    - **[Django 로컬 서버 시작]** python manage&#46;py runserver

### 2.5 Django의 Project & App

- 하나의 Project == 하나의 Web Site
- Project 안의 의미있는 기능들을 **각각의 App으로 관리**

    ![Project와 App의 관계](../img/lecture2(3).png)

- Django 안의 파일들에 대한 간단한 설명
    - Project
        | 파일명 | 내용 |
        | --- | --- |
        | setting&#46;py | 전체 프로젝트를 관리하는 설정 파일 (자주 볼 파일 1)  |
        | urls&#46;py | 프로젝트의 URL 관리 파일 (자주 볼 파일 2) |
        | wsgi&#46;py <br /> asgi&#46;py | 프로젝트를 서비스하기 위한 파일 (배포할 때 아니면 볼 일 없는 파일) |
        | 	&#95;&#95;init&#95;&#95;&#46;py | 해당 디렉토리가 Python Package의 일부입을 Python에게 알려주는 파일 |
    - App
        | 파일명 | 설명 |
        | --- | --- |
        | view&#46;py | 웹 요청을 받고, 전달받은 데이터를 처리해서 가공하는 파일 (자주 볼 파일 3) |
        | models&#46;py | Database와 관련된 다양한 역할 수행 (자주 볼 파일 4) |
        | admin&#46;py | 관리자 관련 파일 |
        | apps&#46;py | Project에게 App의 존재를 알려줄 때 활용되는 파일 |

### 2.6 Home 페이지 출력하기

1. **settings&#46;py**

    Project에게 App의 존재 알리기

2. **templates**

    User에게 보여줄 HTML 파일 만들기

3. **views&#46;py**

    요청이 들어오면 HTML 파일을 열어주는 함수 정의

4. **urls&#46;py**

    url 요청을 views와 연결하기

### 2.7 Django 프로젝트 실습

1. Github repository 생성
2. VS Code 터미널 생성 → `ctrl + shift + p` 누르고 `Terminal Select Default Shell` 입력 →  `enter` → `Git Bash` 선택
3. 폴더를 열고 `repository` 를 clone 할 폴더 선택

    (폴더명과 repository명을 동일하게 해주는 게 좋아요 🙂)

4. 터미널에 repository에 있는 명령어 복사해서 붙여넣기

    ```bash
    echo "/*Add Repository contents*/" >> README.md
    git init
    git add README.md
    git commit -m "first commit"
    git remote add origin /*Repository URL*/
    git push -u origin master
    ```

5. `.gitignore` 파일 생성 후 `gitignore.io` 접속하고, 아래의 이미지와 같이 입력하고 생성 버튼을 누르면

    ![gitignore.io 생성창 입력 내용](../img/lecture2(4).png)

    알 수 없는 글이 떠요!! 😮

    ![.gitignore 내용](../img/lecture2(5).png)

    이 내용을 복사해서 `.gitignore` 파일에 붙여넣고 `venv` 도 추가로 입력

    ![venv 입력 위치](../img/lecture2(6).png)
    
6. Django를 사용하기 위한 기본 설정

    ```bash
    # 가상환경 생성
    py -m venv venv

    # 가상환경 실행
    source venv/Scripts/activate

    # Django 설치
    pip install django

    # pip upgrade
    py -m pip install --upgrade pip
    ```

7. Django Project 생성

    ```bash
    # Django 프로젝트 생성
    django-admin startproject dreamaryproject .

    # Local Server 실행시키는 방법
    py manage.py runserver
    ```

8. Django App 생성

    ```bash
    # dreamaryproject의 app 생성
    py manage.py startapp page
    ```

9. App이 생성되었음을 Project에 알려줘야해요!
    - dreamaryproject 폴더 안의 `setting.py`를 다음과 같이 `'page.apps.PageConfig'` 를 추가하여 수정

        ![setting.py 수정](../img/lecture2(7).png)

    - `page.apps.PageConfig` 라고 써도 되고, `page` 라고 써도 되는데, 첫 번째 방식으로 쓰는 것이 정석!!!

        (page 폴더 안의 appspy라는 파일의 PageConfig class를 알려주는 거라고 생각하면 됩니다 ^0^)

10. page 폴더에 `templates` 폴더 추가를 추가하고 `home.html` 을 생성

    (templates는 html 파일 저장 폴더)

    ![파일 생성 목록](../img/lecture2(8).png)

11. `home.html` 파일에서 `! + Tab` 을 누르면 html 양식이 자동 생성!

    이제 내용을 변경해볼까요!! 😊

    ```html
    <!DOCTYPE html>
    <!-- 언어를 한국어로 변경 -->
    <html lang="ko">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <!-- title 변경 -->
        <title>Dreamary - 헤어 O2O 서비스</title>
    </head>
    <body>
        <!-- body에 내용 추가 -->
        Django가 돌아간다!!
    </body>
    </html>
    ```

12. page 폴더의 `views.py` 파일을 다음과 같이 변경

    ```python
    from django.shortcuts import render

    # Create your views here.

    def home(request):
        # request가 들어오는 경우 home.html을 return
        return render(request, 'home.html')
    ```

13. dreamaryproject 폴더의 `urls.py` 파일을 다음과 같이 변경

    ```python
    from django.contrib import admin
    from django.urls import path

    # views.py 파일 연결
    from page import views

    urlpatterns = [
        path('admin/', admin.site.urls),
        # '' url이 들어오면 views.py의 home 함수 실행를 실행시킬거고, 이 path를 home이라고 부를거야! ^0^
        path('', views.home, name = "home"),
    ]
    ```

14. `py manage.py runserver` 를 통해 실행시켜볼까요 😊

    ![page 실행 화면](../img/lecture2(9).png)

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
