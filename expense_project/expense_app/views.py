from django import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.db.models import Sum
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializer import *
from .permissions import IsOwner


class ExpenseViewSet(viewsets.ModelViewSet):

    serializer_class = (ExpenseSerializer)

    permission_classes = [
        IsAuthenticated,
        IsOwner
    ]

    def get_queryset(self):

        return Expense.objects.filter(
            user=self.request.user
        )

    def perform_create(self,serializer):

        serializer.save(
            user=self.request.user
        )



@api_view(["GET"])
def monthly_summary(request):

    total = Expense.objects.filter(
        user=request.user
    ).aggregate(
        total_spent=Sum("amount")
    )

    return Response(
        total
    )

