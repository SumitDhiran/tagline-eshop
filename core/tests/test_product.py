from .test_setup import TestSetUp,User,Product,Purchase
from django.urls import reverse
from rest_framework import status

class TestProduct(TestSetUp):
    product = Product.objects.first()
    product_list_url = reverse('product-list')
    product_detail_url = reverse('product-detail',kwargs={'pk':product.id})
    product_available_products_url = reverse('product-available-products')

    def get_data(self):
        data = {
            "name": "test_product",
            "description": "test_product",
            "price": "299",
            "type": "Available"
        }

        return data

    def test_get_product(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

        res=self.client.get(self.product_list_url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_post_product(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

        res=self.client.post(self.product_list_url, self.get_data(), format='json')
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_get_single_product(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

        res=self.client.get(self.product_detail_url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_put_single_product(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

        res=self.client.put(self.product_detail_url, self.get_data(), format='json')
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_patch_single_product(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

        res=self.client.patch(self.product_detail_url, self.get_data(), format='json')
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_delete_single_product(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

        res=self.client.delete(self.product_detail_url)
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)

    def test_product_available_products(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

        res=self.client.get(self.product_available_products_url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)