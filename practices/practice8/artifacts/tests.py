from django.test import TestCase
from rest_framework.test import APIClient
from .models import Artifact


class ArtifactTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.artifact_data = {
            "name": "Test Artifact",
            "description": "Test Artifact Description",
            "rarity": "Common"
        }
        self.invalid_artifact_data = {
            "name": "Test Artifact",
            "description": "Test Artifact Description"
        }

    def test_create_artifact(self):
        response = self.client.post('/artifacts/', self.artifact_data)
        self.assertEqual(response.status_code, 201)

    def test_create_artifact_invalid_data(self):
        response = self.client.post('/artifacts/', self.invalid_artifact_data)
        self.assertEqual(response.status_code, 400)

    def test_get_artifacts_list(self):
        response = self.client.get('/artifacts/')
        self.assertEqual(response.status_code, 200)

    def test_get_artifact_detail(self):
        artifact = Artifact.objects.create(**self.artifact_data)
        response = self.client.get(f'/artifacts/{artifact.id}/')
        self.assertEqual(response.status_code, 200)

    def test_update_artifact(self):
        artifact = Artifact.objects.create(**self.artifact_data)
        updated_data = {
            "name": "Updated Artifact Name",
            "description": "Updated Artifact Description",
            "rarity": "Rare"
        }
        response = self.client.put(f'/artifacts/{artifact.id}/', updated_data)
        self.assertEqual(response.status_code, 200)

    def test_delete_artifact(self):
        artifact = Artifact.objects.create(**self.artifact_data)
        response = self.client.delete(f'/artifacts/{artifact.id}/')
        self.assertEqual(response.status_code, 204)
