from django.db import models
from django.conf import settings

TRANSACTION_TYPE = [
    ('income', 'Income'),
    ('expense', 'Expense'),
]

class Transaction(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='transactions'
    )

    amount = models.DecimalField(max_digits=10, decimal_places=2)

    type = models.CharField(max_length=10, choices=TRANSACTION_TYPE)

    category = models.CharField(max_length=50)

    date = models.DateField()

    notes = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.type} - {self.amount}"