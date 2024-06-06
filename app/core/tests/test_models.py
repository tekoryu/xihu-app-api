"""
Tests for models
"""
from decimal import Decimal

from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models

class ModelTests(TestCase):
    """Test models"""

    def test_create_user_with_email(self):
        """"Test creating a new user with email"""
        email = 'test@example.com'
        password = 'testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test email is normalized for new users."""
        sample_emails = [
            ['test1@EXAMPLE.com', 'test1@example.com'],
            ['Test2@Example.com', 'Test2@example.com'],
            ['TEST3@EXAMPLE.com', 'TEST3@example.com'],
            ['test4@example.com', 'test4@example.com'],
        ]

        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email, 'sample123')
            self.assertEqual(user.email, expected)

    def test_new_user_without_email_raises_error(self):
        """ Tests that creating a a user without an email raises a
        ValueError."""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'sample123')

    def test_create_super_user(self):
        """Test creating a super user."""
        user = get_user_model().objects.create_superuser(  # noqa
            'test@example.com',
            'test123',
        )

    def test_create_recipe(self):
        """Test creating a recipe."""
        user = get_user_model().objects.create_user(
            'test@example.com',
            'testpass123'
        )

        recipe = models.Recipe.objects.create(
            user=user,
            title='Sample Recipe Name',
            time_minutes=5,
            price=Decimal('5.50'),
            description='Sample Recipe Description',
        )

        self.assertEqual(str(recipe), recipe.title)