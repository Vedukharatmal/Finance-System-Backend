from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Transaction

User = get_user_model()

class TransactionTest(TestCase):
    def test_create_transaction(self):
        user = User.objects.create(username='test', password='1234')
        transaction = Transaction.objects.create(
            user=user,
            amount=100,
            type='expense',
            category='food',
            date='2026-04-01'
        )
        self.assertEqual(transaction.amount, 100)