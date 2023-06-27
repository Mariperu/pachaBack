# Django
from django.test import TestCase

# Python
import json

# Django Rest Framework
from rest_framework.test import APIClient
from rest_framework import status

# Models
from songs.models import Song


class SongTestCase(TestCase):
    def test_create_song(self):
        client = APIClient()
        test_song = {"id": 1, "name": "yellow"}
        response = client.post("/api/songs/", test_song, format="json")
        result = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("name", result)
        self.assertEqual(result, test_song)

    def test_update_song(self):
        client = APIClient()
        song = Song.objects.create(
            id=1,
            name="song123",
        )
        test_song_update = {
            "id": 1,
            "name": "yellow",
        }
        response = client.put(f"/api/songs/{song.pk}/", test_song_update, format="json")
        result = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        if "pk" in result:
            del result["pk"]
        self.assertEqual(result, test_song_update)

    def test_delete_song(self):
        client = APIClient()
        song = Song.objects.create(
            id=1,
            name="song123",
        )
        response = client.delete(f"/api/songs/{song.pk}/", format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        song_exists = Song.objects.filter(pk=song.pk)
        self.assertFalse(song_exists)

    def test_get_song(self):
        client = APIClient()

        Song.objects.create(
            id=1,
            name="yellow",
        )

        Song.objects.create(
            id=2,
            name="Paradise",
        )

        response = client.get("/api/songs/")
        result = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        for song in result:
            self.assertIn("id", song)
            self.assertIn("name", song)
            break
