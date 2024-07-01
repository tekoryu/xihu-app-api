"""
Tests for the health check.
"""

from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

class HealthCheckTestCase(TestCase):
    """Test the health check API."""

    def test_health_check(self):
        """Test health check."""
        client = APIClient()
        url = reverse('health_check')
        res = client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
