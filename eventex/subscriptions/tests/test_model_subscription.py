from datetime import datetime

from django.test import TestCase
from eventex.subscriptions.models import Subscription


class SubscriptionsModelTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name='Ramiro Alvaro',
            cpf='2345678901',
            email='ramiroalvaro@hotmail.com',
            phone='31-99138-7178'
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Subscription.objects.exists())

    def test_create_at(self):
        """Subscription must have an auto create at attr."""
        self.assertIsInstance(self.obj.create_at, datetime)