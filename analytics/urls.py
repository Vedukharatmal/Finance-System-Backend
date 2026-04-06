from django.urls import path
from .views import SummaryView, CategoryBreakdownView

urlpatterns = [
    path('summary/', SummaryView.as_view()),
    path('category-breakdown/', CategoryBreakdownView.as_view()),
]