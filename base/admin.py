from django.contrib import admin
from .models import Transaction
# Register your models here.
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('title', 'amount', 'date', 'transaction_type')

admin.site.register(Transaction, TransactionAdmin)
