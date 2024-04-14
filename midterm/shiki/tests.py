from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Genre
from .serializers import *


class GenreAPITest(APITestCase):
    def setUp(self):
        self.genre = Genre.objects.create(name='Test Genre', description='Test Description')

    def test_genre_list(self):
        url = reverse('shiki:genre-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_genre_detail(self):
        url = reverse('shiki:genre-detail', kwargs={'pk': self.genre.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_genre_create(self):
        url = reverse('shiki:genre-create')
        data = {'name': 'New Genre', 'description': 'New Description'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)

    def test_genre_update(self):
        url = reverse('shiki:genre-update', kwargs={'pk': self.genre.pk})
        data = {'name': 'Updated Genre', 'description': 'Updated Description'}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, 200)

    def test_genre_delete(self):
        url = reverse('shiki:genre-delete', kwargs={'pk': self.genre.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)
