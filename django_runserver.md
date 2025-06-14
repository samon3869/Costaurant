# 🌐 Django 개발 서버(Live Server) 실행 방법

Django는 개발 중에 **내장된 웹 서버**를 제공하여, 빠르게 결과를 확인할 수 있도록 돕습니다.

---

## ✅ 1. 기본 서버 실행

```bash
python manage.py runserver
```

- 실행 후 접속 주소: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

> ⚠️ `ALLOWED_HOSTS` 오류가 발생하면, `settings.py`에서 다음과 같이 수정하세요:

```python
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']
```

또는 모든 호스트 허용 (개발용):

```python
ALLOWED_HOSTS = ['*']
```

---

## ✅ 2. 포트를 변경하고 싶을 때

```bash
python manage.py runserver 8080
# → http://127.0.0.1:8080/
```

---

## ✅ 3. 외부 장치(스마트폰 등)에서 접속 가능하게

```bash
python manage.py runserver 0.0.0.0:8000
```

- 접속 주소: `http://<컴퓨터 IP>:8000`
- 예: `http://192.168.0.5:8000`

`ALLOWED_HOSTS`에 IP 또는 '*' 포함 필요:

```python
ALLOWED_HOSTS = ['*']
```

---

## ✅ 4. 코드 변경 시 자동 반영

- `runserver`는 기본적으로 코드 변경을 감지하여 **자동 재시작**합니다.
- 하지만 HTML 파일 등은 브라우저에서 **수동 새로고침**이 필요할 수 있습니다.

---

## 🚀 참고: 프론트엔드까지 자동 새로고침 하고 싶다면?

[LiveReload 플러그인](https://github.com/tj/django-livereload-server) 등을 활용하면
HTML, CSS, JS 변경 시 자동으로 브라우저 새로고침이 가능합니다.
