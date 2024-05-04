import pytest
from app.models import Test

@pytest.mark.django_db
def test_create_test():
    data = {'test': 'My test data'}
    response = client.post('/tests/', data, format='json')
    assert response.status_code == 201
    assert Test.objects.count() == 1
    assert Test.objects.get().test == 'My test data'