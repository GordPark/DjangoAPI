from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Product
import json

# GET: 서버로부터 데이터를 요청할 때 사용
# response = self.client.get('/some-url/')
# POST: 서버에서 데이터를 생성하도록 요청할 때 사용
# response = self.client.post('/some-url/', {'key': 'value'}, format='json')
# PUT: 서버에 데이터를 갱신하도록 요청할 때 사용
# response = self.client.put('/some-url/', {'key': 'updated-value'}, format='json')
# PATCH: d서버에 데이터의 부분 갱신을 요청할 때 사용
# response = self.client.patch('/some-url/', {'key': 'partially-updated-value'}, format='json')
# DELETE: 서버에 데이터를 삭제하도록 요청할 때 사용
# response = self.client.delete('/some-url/')
# 로그인: 테스트 시 사용자 인증이 필요할 때 로그인 시물레이션
# self.client.login(username='username', password='password')
#  로그아웃: 로그인된 사용자를 로그아웃
# self.client.logout()
# 테스트 응답에서 HTTP 상태 코드를 검증하여 API가 예상대로 동작하는지 확인
# self.assertEqual(response.status_code, 200)
# 응답 받은 데이터를 검증하여 API가 정확한 값을 반환하는지 확인
# self.assertEqual(response.data['key'], 'expected-value')
# follow: True로 설정하면 302 리다이렉트
# response = self.client.get('/some-url/', follow=True)
# Secure Requests: https 요청을 시뮬레이션하려면 secure=True를 사용
# response = self.client.get('/some-url/', secure=True)

class ProductTests(APITestCase):
    def test_create_product(self):
        """
        새로운 제품을 생성하고 응답을 검증합니다.
        """
        url = reverse('product_list')
        data = {'name': 'Test Product', 'price': 20, 'description':"good", 'in_stock':True}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 1)
        self.assertEqual(Product.objects.get().name, 'Test Product')

    def test_get_product(self):
        """
        제품 목록을 가져오고 결과를 검증합니다.
        """
        response = self.client.get(reverse('product_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        


    def test_delete_product(self):
        """
        특정 제품을 삭제하고 응답을 검증합니다.
        **문제**: 'Products' API를 통해 특정 제품을 삭제하는 API 엔드포인트를 
        테스트하는 코드를 작성하세요.

        - 테스트를 위해 임시로 제품을 하나 생성합니다.(Product.objects.create)
        - url을 구성합니다. (reverse(주소, args=[삭제 대상 id]
        - 요청을 보냅니다. (django에서 테스트용으로 self.client를 이용합니다.)
        """
        product = Product.objects.create(name="Test Product", price=30)
        url = reverse('product_detail',args=[product.id])
       
        response = self.client.get(url,format='json')

        self.assertEqual(response.status_code, 200)
        # response의 내용들을 딕셔너리로 만듬
        response_data = json.loads(response.content.decode('utf-8')) 
        # json() josn형식으로 바꾸고 딕셔너리가 된다
        # 결과가 똑같음
        self.assertEqual(response.json()['price'], '200')
        

        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Product.objects.count(), 0)
        # self.assertEqual(response.status_code, 200)


    def test_get_API(self):
        """
        **문제**: 'Products' API를 통해 특정 제품의 정보를 조회하는 API 엔드포인트를 테스트하는 코드를 작성하세요.

        - 응답 코드가 200인지(정상응답) 확인
        - 응답받은 Product의 name 속성이 처음에 넣은 name 속성과 일치하는지 확인
        """
        def setUP(self):
            self.product = Product.objects.create(name="Test Product", price=30)
            self.url = reverse('product_detail',args=[self.product.id])

        def test_retrieve_product(self):
            response = self.client.get(self.url)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            # 응답내용을 딕셔너리 형태로 변환
            response_data = json.loads(response.content.decode('utf-8')) 
            # 바이트 문자열을 디코딩하여 JSON으로 변환
            self.assertEqual(response_data['name', 'Test Product'])

