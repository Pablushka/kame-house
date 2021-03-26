from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.contrib.auth.models import User
import json

class RegistrationTestCase(APITestCase):

    def test_api_availability(self):
        response = self.client.get('/api/')
        self.assertEqual(response.status_code, status.HTTP_200_CREATED)
