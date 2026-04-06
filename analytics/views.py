from rest_framework.views import APIView
from rest_framework.response import Response
from transactions.models import Transaction
from django.db.models import Sum
from rest_framework.permissions import IsAuthenticated

class SummaryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        transactions = Transaction.objects.filter(user=request.user)

        income = transactions.filter(type='income').aggregate(Sum('amount'))['amount__sum'] or 0
        expense = transactions.filter(type='expense').aggregate(Sum('amount'))['amount__sum'] or 0

        return Response({
            "total_income": income,
            "total_expense": expense,
            "balance": income - expense
        })
    
class CategoryBreakdownView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = (
            Transaction.objects
            .filter(user=request.user, type='expense')
            .values('category')
            .annotate(total=Sum('amount'))
        )
        return Response(data)