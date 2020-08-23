## 5. Django로 나를 소개해볼게 #2

### 5.1 [복습] Django로 나를 소개해볼게 #1

- **Model 이란?**

    데이터에 접속하고 관리하도록 도와주는 객체

- **Model 생성 & 적용**

    Model 생성 → DB가 알아듣도록 번역 → 번역한 내용을 DB에 적용

- **Admin**

    Django는 웹 서비스 관리를 위한 **Admin 기능 기본 제공**

### 5.2 QuerySet 이란?

- 전달받은 모델의 객체 목록

    ![QuerySet](../img/lecture5(1).png)

- veiws&#46;py

    ```python
    # Model의 존재 알려주기
    from .models import Designer

    #Q= Querset을 Templates로 보내기
    def home(request):
        # Designer.objects.all()는 method!
        designers = Designer.objects.all()
        return render(request, 'home.html', {'designers':designers})
    ```

### 5.3 Detail Page 구현

- 아마 이런 의문이 들 거예요!

    각각의 글을 어떻게 분류하지?
    urls.py에서 글마다 Path를 만들어야 하는 건가?
    만약 없는 글을 불러오려고 하면 어쩌지?

- 이러한 의문은 `PK (Primary Key), Path Convertor, get_object_or_404` 로 해결 할 수 있어요

### 5.4 PK (Primary Key)

- Model을 통해 생성된 객체들을 구분할 수 있는 "고유한" Key

    ![PK](../img/lecture5(2).png)

### 5.5 Path Convertor

- 여러 객체의 url을 "계층적으로" 다룰 수 있도록 도와주는 도구

    ![Path Convertor](../img/lecture5(3).png)

- urls&#46;py

    ```python
    path('profile/<int:designer_id>/', views.detail, name = "detail"),
    ```

- Template

    ```html
    {% url 'detail' designer.id %}
    ```

### 5.6 get_object_or_404

- Object를 가져오려 했는데 없을 경우 나타나는 에러
- views&#46;py

    ⚠️ views.py의 pk 변수명과 urls.py의 변수명은 같아야 함!

    ```python
    from django.shortcuts import render, get_object_or_404

    def detail(request, designer_id):
        designer = get_object_or_404(Designer, pk = designer_id)
        return render(request, 'detail.html', {'designer' : designer}
    ```

### 5.7 Detail Page 구현 정리

![Detail Page](../img/lecture5(4).png)

### 5.8 Django 프로젝트 실습하기

**시작 전에 가상환경 키는 것 잊지 말기!! 😉**

1. views에서 model을 알려주고 queryset을 templates로 보내기 위해 `veiws.py` 에 다음과 같이 내용을 추가해줍니다.

    ```python
    from django.shortcuts import render

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
    ```

2. queryset을 활용해 프로필이 뜨도록 `home.html` 을 수정해줍니다.

    ```html
    <div class="album py-5 bg-light">
        <div class="container">
            <div class="card-columns">
                {% for designer in designers %}
                <div class="card mb-4 shadow-sm">
                    <!-- Image -->
                    <!-- 이미지가 있는 경우에는 보여주고 아닌 경우 svg로 대체-->
                    {% if designer.image %}
                    <img src="{{ designer.image.url}}" alt="Designer Image" class="card-img-top" />
                    {% else %}
                    <svg class="bd-placeholder-img card-img-top" width="100%" height="225" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice" focusable="false" role="img" aria-label="Placeholder: Thumbnail">
                        <title>Dreamary</title>
                        <rect width="100%" height="100%" fill="#55595c" /><text x="50%" y="50%" fill="#eceeef"
                            dy=".3em">Profile</text>
                    </svg>
                    {% endif %}
                    <div class="card-body">
                        <h4 class="card-title">{{ designer.name }}</h4>
                        <h6 class="card-text">{{ designer.address }}</h6>
                        <br />
                        <p class="card-text">{{ designer.description }}</p>
                    </div>
                </div>
                {% endfor %}
            </div>
        </div>
    </div>
    ```

    변경된 내용이 적용되었는지 확인해볼까요? ☺️

    ![QuerySet을 활용해 프로필이 뜨도록 수정](../img/lecture5(5).png)

3. admin에 객체를 추가하면 자동으로 반영되는지 확인해봅시다.
    - 토끼 친구를 추가해볼게요 🐰

        ![admin에서 토끼 추가](../img/lecture5(6).png)

    - 추가되었네요!! 🥰

        ![웹페이지에 토끼가 추가된 모습](../img/lecture5(7).png)

4. `home.html` 에서 버튼을 누르면 `detail` 페이지로 넘어가도록 내용을 수정합니다.

    ```html
    <div class="album py-5 bg-light">
        <div class="container">
            <div class="card-columns">
                {% for designer in designers %}
                <div class="card mb-4 shadow-sm">
                    <!-- Image -->
                    <!-- 이미지가 있는 경우에는 보여주고 아닌 경우 svg로 대체-->
                    {% if designer.image %}
                    <img src="{{ designer.image.url}}" alt="Designer Image" class="card-img-top" />
                    {% else %}
                    <svg class="bd-placeholder-img card-img-top" width="100%" height="225" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice" focusable="false" role="img" aria-label="Placeholder: Thumbnail">
                        <title>Dreamary</title>
                        <rect width="100%" height="100%" fill="#55595c" /><text x="50%" y="50%" fill="#eceeef" dy=".3em">Profile</text>
                    </svg>
                    {% endif %}
                    <div class="card-body">
                        <h4 class="card-title">{{ designer.name }}</h4>
                        <h6 class="card-text">{{ designer.address }}</h6>
                        <br />
                        <p class="card-text">{{ designer.description }}</p>
                        <!-- 내용이 추가분 부분 -->
                        <div class="d-flex justify-content-between align-items-center">
                            <div class="btn-group">
                                <a href="{% url 'detail' designer.id %}" class="btn btn-sm btn-outline-secondary">자세히 알아보기</a>
                            </div>
                        </div>
                    </div>
                </div>
                {% endfor %}
            </div>
        </div>
    </div>
    ```

    `urls.py`도 수정해줍니다.

    ```html
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', views.home, name = "home"),
        path('introduce/', views.introduce, name = "introduce"),
        path('profile/<int:designer_id>/', views.detail, name = "detail"),
    ] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    ```

    veiws.py를 수정할 때 object가 없는 경우를 대비해 get_object_or_404를 import 하고, detail에 대한 내용을 추가합니다.

    ```python
    from django.shortcuts import render, get_object_or_404
    from .models import Designer

    def home(request):
        designers = Designer.objects.all()
        return render(request, 'home.html', {'designers':designers})

    def introduce(request):
        return render(request, 'introduce.html')

    # pk로 designer_id를 받아옵니다.
    def detail(request, designer_id):
        designer = get_object_or_404(Designer, pk = designer_id)
        return render(request, 'detail.html', {'designer' : designer})
    ```

5. 이제 `detail.html` 을 수정해볼까요? 🙂

    `home.html` 을 복사한 다음 title과 연결된 css, 그리고 main을 수정해줍니다. (header는 삭제해주세요!)

    ```html
    <title>디자이너 세부 프로필</title>

    ...

    <link rel="stylesheet" href="{% static 'css/detail.css' %}" />

    ...

    <main role="main">
            <div class="container">
                <div id="designer" class="row featurette">
                    <div class="col-md-6">
                        <h2 class="featurette-heading">{{ designer.name }}<span id="namedeco" class="text-muted">헤어 디자이너</span></h2>
                        <h5 class="featurette-heading">"{{ designer.address }}" 에서 활동 중입니다.</h5>
                        <p class="lead">{{ designer.description }}</p>
                    </div>
                    <div class="col-md-4">
                        <img src="{{ designer.image.url }}" width="150%" alt="Designer_Profile_Image">
                    </div>
                </div>
            </div>
        </main>
    ```

    변경된 내용이 반영되었는지 확인해봅시다!

    ![자세히 알아보기 버튼이 생성된 모습](../img/lecture5(8).png)

    자세히 알아보기를 누르면 다음과 같은 detail 페이지를 볼 수 있습니다. 😺

    ![자세히 알아보기 버튼을 클릭하면 나오는 모습](../img/lecture5(9).png)

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