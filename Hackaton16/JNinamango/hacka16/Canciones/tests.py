from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
# Create your tests here.

url = '/canciones/'##mismo nombre que en las urls de hacka 16


class CancionesAPITest(APITestCase):

    # def test_create_song(self):

    #     data = {'name': 'test'}
    #     response = self.client.post(url, data)
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #     self.assertEqual(response.data['name'],'test')

    # def test_get_song(self):
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_update_song(self):
    #     response = self.client.post(url, {'name': 'losdelspace'})
    #     song_id = response.data['id']

    #     updated_data = {'name': 'tucuelpomellamaventepolfavo'}

    #     update_response = self.client.put(f'{url}{song_id}/', updated_data)

    #     self.assertEqual(update_response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(update_response.data['name'], 'tucuelpomellamaventepolfavo')

    
    def test_retrieve_song(self):
        song_data = {'name': 'losdelspace'}
        response = self.client.post(url, song_data)
        song_id = response.data['id']
    
        response = self.client.get(f'{url}{song_id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], song_data['name'])