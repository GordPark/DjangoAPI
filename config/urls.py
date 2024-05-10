"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
   openapi.Info(
      title="Products API", # 프로젝트 이름
      default_version='v1', # 프로젝트 버전
      description="Test description", # 해당 문서 설명
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="gord23p@gmail.com"), # 부가정보
        license=openapi.License(name="mit"),     # 부가정보
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')), # 베이스 코드 style api/products/...
    path('apiset/', include('apiset.urls')), # DRF의 장고에서 제공하는 style apiset/products/...
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

# 생성 테이블 이름
# api_product
# apiset_product
