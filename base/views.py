
from django.shortcuts import redirect, render
from .models import Transaction
from base import models 

# Create your views here.
def home(request):
    balance = Transaction.get_balance()
    income = Transaction.get_income()
    expense = Transaction.get_expense()
    context = {
        'balance': balance,
        'income': income,
        'expense': expense,
    }
    return render(request, 'home.html', context)

def add_transaction(request):
    if request.method == 'POST':
        type = request.POST.get('type')
        title = request.POST['title']
        amount = request.POST['amount']
        # date = request.POST['date']
        date = request.POST['date']
        
        
        if type == 'Income':
            transaction = Transaction(title=title, amount=amount, date=date, transaction_type=Transaction.INCOME)
        else:
            transaction = Transaction(title=title, amount=amount, date=date, transaction_type=Transaction.EXPENSE)
        
        transaction.save()
    return redirect('home')

def income_page(request):
    income_tran = Transaction.get_income_transactions()
    balance = Transaction.get_balance()
    income = Transaction.get_income()
    expense = Transaction.get_expense()
    context = {
        'balance': balance,
        'income': income,
        'expense': expense,
        'income_tran': income_tran,
    }
    return render(request, 'income.html', context)

def expense_page(request):
    expense_tran = Transaction.get_expense_transactions()
    balance = Transaction.get_balance()
    income = Transaction.get_income()
    expense = Transaction.get_expense()
    context = {
        'balance': balance,
        'income': income,
        'expense': expense,
        'expense_tran': expense_tran,
    }
    return render(request, 'expense.html', context)