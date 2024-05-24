import json
from rest_framework import status
from rest_framework.test import APIClient
from django.urls import reverse
from myapp.models import Test

client = APIClient()

def test_create_test():
    url = reverse('test-detail', kwargs={'pk': 1})
    data = {'name': 'Test 1', 'description': 'This is a test'}
    response = client.post(url, data, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert Test.objects.count() == 1
    assert Test.objects.get().name == 'Test 1'

def test_get_test():
    test = Test.objects.create(name='Test 2', description='This is another test')
    url = reverse('test-detail', kwargs={'pk': test.pk})
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data['name'] == 'Test 2'

def test_update_test():
    test = Test.objects.create(name='Test 3', description='This is a third test')
    url = reverse('test-detail', kwargs={'pk': test.pk})
    data = {'name': 'Updated Test', 'description': 'This is an updated test'}
    response = client.put(url, data, format='json')
    assert response.status_code == status.HTTP_200_OK
    assert Test.objects.get(pk=test.pk).name == 'Updated Test'

def test_delete_test():
    test = Test.objects.create(name='Test 4', description='This is a fourth test')
    url = reverse('test-detail', kwargs={'pk': test.pk})
    response = client.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert Test.objects.count() == 0
