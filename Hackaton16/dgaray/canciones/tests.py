from rest_framework.test import APITestCase
from rest_framework import status

class ProductAPITest(APITestCase):
    # def test_create_product(self):
    #     url = '/canciones/'
    #     data = {'name': 'Example Product'}

    #     response = self.client.post(url, data)
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #     self.assertEqual(response.data['name'], 'Example Product')

    # def test_get_product_list(self):
    #     url = '/canciones/'
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_product_detail(self):
        # product_id = 14
        # url = f'/canciones/{product_id}/'
        response = self.client.get('http://127.0.0.1:8000/canciones/14/')
        print(response)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertEqual(len(response.data), 1)  # Assuming there is only one product
