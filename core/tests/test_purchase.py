from .test_setup import TestSetUp,User,Product,Purchase
from django.urls import reverse
from rest_framework import status

class TestPurchase(TestSetUp):
    purchase = Purchase.objects.first()
    purchase_list_url = reverse('purchase-list')
    purchase_detail_url = reverse('purchase-detail',kwargs={'pk':purchase.id})
    purchase_user_purchase_url = reverse('purchase-user-purchase')

    def test_get_purchase(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

        res=self.client.get(self.purchase_list_url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_post_purchase(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        data = {
            "product":self.product3.id,
            "purchase_price":"599"
        }

        res=self.client.post(self.purchase_list_url, data, format='json')
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_get_single_purchase(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

        res=self.client.get(self.purchase_detail_url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_get_purchase_user_purchase(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

        res=self.client.get(self.purchase_user_purchase_url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
