from rest_framework.test import APITestCase
from django.urls import reverse
from ..models import User,Product,Purchase

class TestSetUp(APITestCase):

    def setUp(self) -> None:
        self.user_data = {
            "username": "test_user",
            "email": "test_user@example.com",
            "password": "test_user"
        }

        self.register_url = reverse('user-list')
        self.client.post(self.register_url,self.user_data,format='json')

        self.login_url    = reverse('token_obtain_pair')
        self.login_data = {
                            'username': 'test_user',
                            'password': 'test_user'
                    }

        # self.product = Product.objects.all().first()

        res = self.client.post(self.login_url,self.login_data,format='json')
        self.access_token = res.data['access']


        """for get product"""
        self.user = User.objects.first()

        self.product = Product.objects.create(
            owner = self.user,
            name = "initial_test_product",
            description = "initial_test_product",
            price = "499",
            type = "Available"
        )

        """for get purchase"""
        self.user_data2 = {
            "username": "test_user2",
            "email": "test_user2@example.com",
            "password": "test_user2"
        }

        self.client.post(self.register_url,self.user_data2,format='json')
        self.user2 = User.objects.filter(username="test_user2").first()

        self.product2 = Product.objects.create(
            owner = self.user2,
            name = "initial_test_product2",
            description = "initial_test_product2",
            price = "799",
            type = "Available"
        )
        self.purchase = Purchase.objects.create(
            product = self.product2,
            buyer = self.user,
            purchase_price = "699"

        )

        """for post purchase"""
        self.user_data3 = {
            "username": "test_user3",
            "email": "test_user3@example.com",
            "password": "test_user3"
        }

        self.client.post(self.register_url,self.user_data3,format='json')
        self.user3 = User.objects.filter(username="test_user3").first()

        self.product3 = Product.objects.create(
            owner = self.user3,
            name = "initial_test_product3",
            description = "initial_test_product3",
            price = "999",
            type = "Available"
        )


        return super().setUp()