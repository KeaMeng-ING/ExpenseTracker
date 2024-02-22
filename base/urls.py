
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('add-transaction/', views.add_transaction, name='add-transaction'),
    path('income/', views.income_page, name='income'),
    path('expense/', views.expense_page, name='expense'),
]
