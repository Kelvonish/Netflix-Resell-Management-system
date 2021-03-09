from django import forms
from django.forms import ModelForm
from .models import Customer,Netflix_Account,Card



class CardForm(ModelForm):
    class Meta:
        model =Card
        fields = ['card_name','card_number']
        widgets = {
            'card_number':forms.NumberInput(attrs={'type':'number','class':'form-control input-lg'}),
            'card_name':forms.TextInput(attrs={'class':'form-control input-lg'}),
            
        }

class NetflixForm(ModelForm):
    class Meta:
        model =Netflix_Account
        fields = ['email','password','card','amount','creation_date']
        widgets = {
            'email':forms.EmailInput(attrs={'type':'email','class':'form-control input-lg'}),
            'password':forms.TextInput(attrs={'type':'text','class':'form-control input-lg'}),
            'card':forms.Select(attrs={'class':'form-control input-lg'}),
            'amount':forms.NumberInput(attrs={'type':'number','class':'form-control input-lg'}),
            'creation_date':forms.DateInput(attrs={'type': 'date','class':'form-control input-lg'}),
        }


class CustomerForm(ModelForm):
    class Meta:
        model =Customer
        fields = ['name','phone','netflix_account','amount','start_date']
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control input-lg'}),
            'phone':forms.TextInput(attrs={'class':'form-control input-lg'}),
            'netflix_account':forms.Select(attrs={'class':'form-control input-lg'}),
            'amount':forms.NumberInput(attrs={'type':'number','class':'form-control input-lg'}),
            'start_date':forms.DateInput(attrs={'type': 'date','class':'form-control input-lg'}),
        }

