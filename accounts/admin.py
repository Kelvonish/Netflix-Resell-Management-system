from django.contrib import admin
from .models import Netflix_Account,Card,Expense,Customer,Income

admin.site.register(Netflix_Account)
admin.site.register(Card)
admin.site.register(Customer)
admin.site.register(Expense)
admin.site.register(Income)

# Register your models here.
