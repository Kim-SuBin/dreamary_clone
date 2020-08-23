# Django로 나를 소개해볼게 #1

### 4.1 [복습] Django가 관리하는 법

- **URL Path의 구조**

    `path('URL', views 내부의 함수, name="url의 이름"),`

- **Template 언어란?**

    Python 변수 & 문법을 HTML에서 쓸 수 있도록 **Django에서 제공하는 언어**

- **Static File 이란?**

    이미지나 CSS, JS 파일처럼 내용이 고정되어 있어, **응답을 할 때 파일 그래로를 보내주면 되는 파일**

### 4.2 Model이란?

- 데이터에 접속하고 관리하도록 도와주는 객체

    ![Model](../img/lecture4(1).png)

### 4.3 Model 생성 & 적용

- models&#46;py

    ```python
    # 모델명(class)의 첫 글자는 무조건 대문자!!

    class Designer(models.Model):
    	image = models.ImageField(upload_to = 'images/')
    	name = models.CharField(max_length = 50)
    	address = models.CharField(max_length = 255)
    	description = models.TextField()
    ```

- Terminal

    ```bash
    python manage.py makemigrations

    python manage.py migrate
    ```

- django와 데이터베이스는 분리되어 있기 때문에 번역이 필요

    ![django와 데이터베이스는 서로 몰라요!](../img/lecture4(2).png)

    그 역할을 해주는 것이 Terminal의 명령어

    ```bash
    # DB가 알아듣도록 번역
    python manage.py makemigrations (+ App 이름)

    # 번역한 내용을 DB에 적용
    python manage.py migrate (+ App 이름)

    # App 이름을 쓰면 특정 App만 DB가 알아들을 수 있도록 번역 및 적용
    ```

### 4.4 Admin 기능

- Django는 웹 서비스 관리를 위한 admin 기능 기본 제공
- Terminal에 다음 명령어 입력을 통해 생성 가능

    ```bash
    python manage.py createsuperuser
    ```

### 4.5 Admin에게 Model 알려주기

- admin&#46;py

    ```python
    from .models import Designer

    admin.site.register(Designer)
    ```

### Django 프로젝트 실습

1. `models.py` 에 다음과 같은 내용을 추가합니다.

    ```python
    class Designer(models.Model):
    	image = models.ImageField(upload_to = 'images/')
    	name = models.CharField(max_length = 50)
    	address = models.CharField(max_length = 255)
    	description = models.TextField()
    ```

2. `ImageField` 를 사용하기 위해 Pillow 설치합니다.

    ```bash
    py -m pip install Pillow
    ```

3. DB에게 알려줍시다!

    ```bash
    py manage.py makemigrations

    py manage.py migrate
    ```

4. model에 대해 확인해보기 위해 admin을 활용해봅시다 🙂
    - admin 생성

        ```bash
        py manage.py createsuperuser
        ```

        username과 password는 잊지마세요!!

        (email은 선택사항이니 입력하지 않아도 괜찮습니다.)

        ![admin 생성](../img/lecture4(3).png)

    - local server 실행을 통해 `http://127.0.0.1:8000/admin/`에 접속하고 username과 password를 입력하면

        ![name과 password 입력창](../img/lecture4(4).png)

        다음과 같이 페이지를 볼 수 있어요 🤗

        ![admin 페이지 (model을 모르는 상태)](../img/lecture4(5).png)

        admin에게 model이 생겼음을 알려주지 않아서 model에 관한 내용이 추가되지 않았네요 ☹️

5. admin이 model에 대해 알 수 있도록 `admin.py` 를 수정하면

    ```python
    from .models import Designer

    admin.site.register(Designer)
    ```

    admin 페이지에 model에 대한 내용이 추가되었음을 알 수 있어요 ☺️

    ![model을 알게된 admin](../img/lecture4(6).png)

6. admin 페이지에서 내용을 추가해봅시다.

    ![admin 페이지에 내용 추가](../img/lecture4(7).png)

    내용을 입력하고 save를 누르면 다음과 같이 저장된 것을 확인 가능합니다.

    ![admin 페이지에 내용이 저장된 모습](../img/lecture4(8).png)

7. `Designer object(1)` 이라고 뜨는 것보다 입력한 `name` 이 뜨는 것이 보기 더 좋겠죠?! 그러므로 `models.py`를 다음과 같이 수정해줍니다.

    ```python
    from django.db import models

    # Create your models here.

    class Designer(models.Model):
        image = models.ImageField(upload_to='images/')
        name = models.CharField(max_length=50)
        address = models.CharField(max_length=255)
        description = models.TextField()

        ## 이 부분 추가해주세요!
        def __str__(self):
            return self.name
    ```

    admin 페이지를 확인하면 다음과 같이 바뀐 것을 볼 수 있어요 ☺️

    ![name을 알게된 admin](../img/lecture4(9).png)

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
