from django.test import TestCase, Client
from .models import Test

class TestEndpoints(TestCase):
    def setUp(self):
        self.client = Client()

    def test_put_endpoint(self):
        response = self.client.put('/put/', {'test': 'put_test'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('id', response.json())
        self.assertIn('test', response.json())

    def test_post_endpoint(self):
        response = self.client.post('/post/', {'test': 'post_test'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('id', response.json())
        self.assertIn('test', response.json())

    def test_delete_endpoint(self):
        test = Test.objects.create(test='delete_test')
        response = self.client.delete(f'/delete/{test.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Test.objects.filter(id=test.id).count(), 0)

    def test_get_endpoint(self):
        test = Test.objects.create(test='get_test')
        response = self.client.get(f'/get/{test.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('id', response.json())
        self.assertIn('test', response.json())