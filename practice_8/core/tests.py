from django.test import TestCase
from rest_framework.test import APIClient
from .models import Product

# Create your tests here.

class ProductAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.product = Product.objects.create(name='Test Product', price=10.99, description='Test description')

    def test_get_products(self):
        response = self.client.get('/api/products/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_create_product(self):
        data = {'name': 'New Product', 'price': 15.99, 'description': 'New description'}
        response = self.client.post('/api/products/', data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Product.objects.count(), 2)

    def test_update_product(self):
        data = {'name': 'Updated Product', 'price': 20.99, 'description': 'Updated description'}
        response = self.client.put(f'/api/products/{self.product.id}/', data, format='json')
        self.assertEqual(response.status_code, 200)
        self.product.refresh_from_db()
        self.assertEqual(self.product.name, 'Updated Product')

    def test_delete_product(self):
        response = self.client.delete(f'/api/products/{self.product.id}/')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Product.objects.count(), 0)
