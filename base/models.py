from django.db import models
from django.db.models import Sum

# Create your models here.
class Transaction(models.Model):
    INCOME = 'IN'
    EXPENSE = 'EX'
    TRANSACTION_TYPE_CHOICES = [
        (INCOME, 'Income'),
        (EXPENSE, 'Expense'),
    ]

    title = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(
        max_length=2,
        choices=TRANSACTION_TYPE_CHOICES,
        default=EXPENSE,
    )
    date = models.DateTimeField(auto_now_add=True)
    # time = models.TimeField()

    def __str__(self):
        return self.title

    @classmethod
    def get_balance(cls):
        income = cls.objects.filter(transaction_type=cls.INCOME).aggregate(models.Sum('amount'))['amount__sum'] or 0
        expense = cls.objects.filter(transaction_type=cls.EXPENSE).aggregate(models.Sum('amount'))['amount__sum'] or 0
        return round(income - expense,2)

    @classmethod
    def get_income(cls):
        income =  cls.objects.filter(transaction_type=cls.INCOME).aggregate(total=Sum('amount'))['total'] or 0
        return round(income,2)
    
    @classmethod    
    def get_expense(cls):
        expense =  cls.objects.filter(transaction_type=cls.EXPENSE).aggregate(total=Sum('amount'))['total'] or 0
        return round(expense,2)
    
    @classmethod
    def get_income_transactions(cls):
        return cls.objects.filter(transaction_type=cls.INCOME)
    
    @classmethod
    def get_expense_transactions(cls):
        return cls.objects.filter(transaction_type=cls.EXPENSE)
    
