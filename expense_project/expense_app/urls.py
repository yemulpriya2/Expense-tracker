from django.urls import path
from .views import ExpenseViewSet, monthly_summary
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(
    'expenses', 
    ExpenseViewSet, 
    basename='expenses'
)

urlpatterns = [
    path('summary/', monthly_summary, name='monthly-summary'),
]
