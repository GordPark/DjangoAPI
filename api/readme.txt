Django의 기본 기능만을 사용하여 REST API 구현

- config 생성(django-admin startproject config .)
- 새로운 앱 생성(python manage.py startapp api)
- 모델 생성(models.py)
    Product 모델 정의
- 시리얼라이저 정의(seriallizers.py)
    JSON 형식으로 데이터 변환
- 뷰 함수 구현(views.py)
    GET, POST, PUT, DELETE 메소드 구현
- URL 설정(urls.py)
    URL 경로 설정
