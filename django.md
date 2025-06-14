

# 🛠️ 1. Django 프로젝트 기본 구조 설명

`django-admin startproject myproject` 실행 시 생성되는 디렉토리 구조:

```
myproject/
├── manage.py
└── myproject/
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    ├── asgi.py
    └── wsgi.py
```

---

## 📄 각 파일 및 디렉토리 설명

### 📁 외부 `myproject/` (루트 디렉토리)

- 프로젝트의 **전체 루트 폴더**
- 이름은 마음대로 바꿔도 됨

### 📄 `manage.py`

- Django 프로젝트의 **명령줄 도구**
- 예: 서버 실행, 마이그레이션 적용, 테스트 실행 등에 사용
- 내부적으로 `myproject/settings.py`를 설정으로 사용함

```bash
python manage.py runserver
python manage.py migrate
```

---

## 📁 내부 `myproject/` (설정 모듈 디렉토리)

### 📄 `__init__.py`

- 이 디렉토리를 **파이썬 패키지로 인식**하게 만듭니다. python 3.3 버전 이상 부터는 이 파일이 없어도 python 패키지로 인식함

### 📄 `settings.py`

- **프로젝트 전역 설정 파일**
- 데이터베이스, 앱 등록, 미들웨어, 정적 파일 경로 등 설정 포함

### 📄 `urls.py`

- **URL 라우팅 설정 파일**
- URL 경로와 view 함수/클래스를 매핑

### 📄 `asgi.py`

- **ASGI 서버 진입점**
- 비동기 처리 기반의 서버(WebSocket 등)를 위한 설정

### 📄 `wsgi.py`

- **WSGI(WebServer Gateway Interface) 서버 진입점**
- 전통적인 동기 기반 서버(Gunicorn, uWSGI 등)를 위한 설정
- 웹서버와  python 어플리케이션인 Django가 소통하는데 필요한 프로토콜

---

## ✅ 요약

| 파일/디렉토리             | 역할 요약                |
| ------------------------- | ------------------------ |
| `manage.py`             | CLI 명령어 실행용 진입점 |
| `settings.py`           | 전역 설정                |
| `urls.py`               | URL 패턴 등록            |
| `asgi.py` / `wsgi.py` | 서버 배포용 진입점       |
| `__init__.py`           | 패키지 초기화 파일       |


# 🚀 2. Django 앱 기본 구조 설명

`python manage.py startapp myapp` 실행 시 생성되는 디렉토리 구조:

```
myapp/
├── __init__.py
├── admin.py
├── apps.py
├── migrations/
│   └── __init__.py
├── models.py
├── tests.py
└── views.py
```

---

## 📄 각 파일 및 디렉토리 설명

### 📁 `myapp/`
- Django 앱(기능 단위)의 디렉토리
- 하나의 앱은 일반적으로 하나의 기능 또는 도메인을 담당

### 📄 `__init__.py`
- Python에서 해당 디렉토리를 **패키지로 인식**하기 위한 파일

### 📄 `admin.py`
- Django 관리자(admin) 사이트에 모델을 등록하여 **관리 UI 제공**
- 예: `admin.site.register(MyModel)`

### 📄 `apps.py`
- 앱의 구성 클래스 정의
- Django가 이 앱을 인식하고 설정하는 데 사용됨

### 📁 `migrations/`
- 마이그레이션 파일 저장 디렉토리
- 모델 변경 시 자동으로 생성되며, DB 스키마 반영에 사용

#### 📄 `migrations/__init__.py`
- 마이그레이션 디렉토리를 패키지로 인식하기 위한 초기화 파일

### 📄 `models.py`
- 데이터베이스 모델 정의
- ORM으로 클래스 형태로 테이블 구조를 설계

### 📄 `tests.py`
- 앱 단위의 테스트 코드 작성 공간
- Django의 `TestCase` 클래스를 상속받아 단위 테스트 구현 가능

### 📄 `views.py`
- 사용자 요청을 처리하는 로직을 정의
- HTML 렌더링, JSON 반환 등 실제 처리 흐름 담당

---

## ✅ 다음 단계

앱을 생성한 뒤에는 **`settings.py`의 `INSTALLED_APPS`에 앱 이름을 추가해야** Django가 앱을 인식합니다:

```python
# myproject/settings.py
INSTALLED_APPS = [
    ...
    'myapp',
]
```




🎥 [Django 작동방식 및 MVT 컨셉](https://www.youtube.com/watch?v=xFkzKxQz9gE)
