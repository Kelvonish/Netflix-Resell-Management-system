from django.db import models

# Create your models here.

class Card(models.Model):
    card_name = models.CharField(max_length=100)
    card_number = models.CharField(max_length=100)
    initial_date = models.DateTimeField(auto_now=True)
    updated_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.card_name

    

class Netflix_Account(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=50)
    card=models.ForeignKey(Card,null=True,blank=True, on_delete=models.SET_NULL)
    amount = models.IntegerField()
    creation_date = models.DateField()
    renewal_date = models.DateField()
    is_active = models.BooleanField()
    initial_date = models.DateTimeField(auto_now=True)
    updated_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.IntegerField()
    netflix_account = models.ForeignKey(Netflix_Account,null=True,blank=True, on_delete=models.SET_NULL)
    amount = models.IntegerField()
    start_date=models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField()
    initial_date = models.DateTimeField(auto_now=True)
    updated_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Income(models.Model):
    customer = models.ForeignKey(Customer,null=True,blank=True,on_delete=models.SET_NULL)
    netflix_account = models.ForeignKey(Netflix_Account,null=True,blank=True,on_delete=models.SET_NULL)
    amount = models.IntegerField()
    creation_date = models.DateField()
    def __str__(self):
        return self.customer.name
    


class Expense(models.Model):
    netflix_account = models.ForeignKey(Netflix_Account,null=True,blank=True,on_delete=models.SET_NULL)
    card = models.ForeignKey(Card,null=True,blank=True,on_delete=models.SET_NULL)
    amount = models.IntegerField()
    creation_date = models.DateField()

    def __str__(self):
        return self.netflix_account.email

    





