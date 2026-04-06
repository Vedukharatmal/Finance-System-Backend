from rest_framework import viewsets
from .models import Transaction
from .serializers import TransactionSerializer
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsAdmin

class TransactionViewSet(viewsets.ModelViewSet):
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)