from django.shortcuts import render,redirect
from .forms import CustomerForm, NetflixForm, CardForm
from .models import Customer, Netflix_Account, Card, Expense, Income
from django.utils.dateparse import parse_date
from dateutil.relativedelta import relativedelta
from datetime import date
from django.shortcuts import get_object_or_404
from django.contrib import messages
import datetime
from django.db.models import Sum
import calendar
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.decorators import login_required



# Create your views here.

@login_required(login_url="login")
def index(request):
    totalUsers = Customer.objects.all().count()
    totalAccounts = Netflix_Account.objects.all().count()
    sahii = datetime.datetime.now()
    today = date.today()
    nextWeek = today+relativedelta(weeks=+1)
    upcoming_renewal_customer= Customer.objects.filter(end_date__gte=today,end_date__lte=nextWeek)
    upcoming_netflix_renewals = Netflix_Account.objects.filter(renewal_date__gte=today,renewal_date__lte=nextWeek)
    currentMonth = datetime.datetime.now().month
    currentYear = datetime.datetime.now().year
    income = Income.objects.filter(creation_date__month=currentMonth,creation_date__year=currentYear).aggregate(Sum('amount'))
    expense = Expense.objects.filter(creation_date__month=currentMonth,creation_date__year=currentYear).aggregate(Sum('amount'))
    


    context={
        'totalUsers': totalUsers,
        'totalAccounts':totalAccounts,
        'time':sahii,
        'today':today,
        'renewalCustomers':upcoming_renewal_customer,
        'renewalNetflix':upcoming_netflix_renewals,
        'income':income,
        'expense':expense,
        'month': calendar.month_name[currentMonth],
        'year': currentYear
    }    

    return render(request, "index.html", context)

@login_required(login_url="login")
def netflix(request):
    if request.method == 'POST':
        form = NetflixForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            amount = form.cleaned_data['amount']
            card=form.cleaned_data['card']
            creation_date = form.cleaned_data['creation_date']
            renewal_date = creation_date+relativedelta(months=+1)
            unique = Netflix_Account.objects.filter(email__exact=email)
            if unique:
                 messages.warning(request, "Netflix account with that email already exists in the system")
            else:
                s = Netflix_Account(email=email, password=password,
                                card=form.cleaned_data['card'], amount=amount, creation_date=creation_date, renewal_date=renewal_date, is_active=True)
            
                s.save()
                e = Expense(card=card,amount=amount,creation_date=creation_date,netflix_account=s)
                e.save()
                messages.success(request,"Superb! Netflix account created successfully")

        else:
            messages.warning(request,form.errors)
            

    all = Netflix_Account.objects.all()

    due_accounts = all.filter(renewal_date__lte=date.today())
    active_accounts = all.filter(renewal_date__gt=date.today())

    n = NetflixForm()
    n.initial['amount']=1200
    context = {
        'active_accounts': active_accounts,
        'due_accounts': due_accounts,
        'NetflixForm': n
    }
    return render(request, 'accounts.html', context)

@login_required(login_url="login")
def customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():

            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            netflix_account = form.cleaned_data['netflix_account']
            amount=form.cleaned_data['amount']
            start_date = form.cleaned_data['start_date']
            end_date = start_date+relativedelta(months=+1)
            unique = Customer.objects.filter(phone__exact=phone)
            if unique:
                messages.warning(request, "Customer with that phone number already exists in the system")
            else:
                num = Customer.objects.filter(netflix_account__exact=netflix_account).count()
                if num>=4:
                    messages.warning(request,"The netflix account selected has the maximum number of 4 users")
                else:

                    s = Customer(name=name, phone=phone, netflix_account=netflix_account, amount=form.cleaned_data['amount'],
                         start_date=start_date, end_date=end_date, is_active=True)
                    s.save()
                    
                    e=Income(amount=amount,netflix_account=netflix_account,customer=s,creation_date=start_date)
                    e.save()
                    messages.success(request, "Superb, The account is created!")
            
               
        else:
            messages.warning(request,form.errors)

    all = Customer.objects.all()

    due_accounts = all.filter(end_date__lte=date.today())
    active_accounts = all.filter(end_date__gt=date.today())

    customer = CustomerForm()
    customer.initial['amount']=500
    context = {
        'active_accounts': active_accounts,
        'due_accounts': due_accounts,
        'customerForm': customer
    }
    return render(request, 'customers.html', context)

@login_required(login_url="login")
def editCustomer(request, pk):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            u = Customer.objects.get(id=pk)
            u.name = form.cleaned_data['name']
            u.phone = form.cleaned_data['phone']
            u.netflix_account = form.cleaned_data['netflix_account']
            u.amount =form.cleaned_data['amount']
            u.start_date = form.cleaned_data['start_date']
            u.end_date = form.cleaned_data['start_date']+relativedelta(months=+1)

            u.save()
            messages.success(request,"Superb! Customer details updated")
            return redirect('customers')

        else:
            messages.warning(request,form.errors)

    u = get_object_or_404(Customer,id=pk)
    form = CustomerForm()
    form.initial['name']= u.name
    form.initial['phone']=u.phone
    form.initial ['netflix_account']=u.netflix_account
    form.initial['amount']=u.amount
    form.initial['start_date']=u.start_date
    context = {
        'user': u,
        'form': form

    }

    return render(request, 'editCustomer.html', context)
@login_required(login_url="login")
def editNetflix(request,pk):
    if request.method == 'POST':
        form = NetflixForm(request.POST)
        
        if form.is_valid():
            u = Netflix_Account.objects.get(id=pk)
            u.email = form.cleaned_data['email']
            u.password = form.cleaned_data['password']
            u.card = form.cleaned_data['card']
            u.amount =form.cleaned_data['amount']
            u.creation_date = form.cleaned_data['creation_date']
            u.renewal_date = form.cleaned_data['creation_date']+relativedelta(months=+1)

            u.save()
            messages.success(request,"Superb! Netflix Account details updated")
            return redirect('accounts')

        else:
            messages.warning(request,form.errors)
    u = get_object_or_404(Netflix_Account,id=pk)
    form = NetflixForm()
    form.initial['email']= u.email
    form.initial['password']=u.password
    form.initial ['card']=u.card
    form.initial['amount']=u.amount
    form.initial['creation_date']=u.creation_date
    context = {
        'account': u,
        'form': form

    }

    return render(request, 'editNetflix.html', context)
@login_required(login_url="login")
def deleteCustomer(request,pk):
    if request.method=="POST":
        object = Customer.objects.get(id=pk)
        object.delete()
        messages.success(request, 'Customer deleted successfully')
        return redirect('customers')
    else:
        return render(request, "deleteAccount.html")

@login_required(login_url="login")
def deleteNetflix(request,pk):

    if request.method=="POST":
        object = Netflix_Account.objects.get(id=pk)
        object.delete()
        messages.success(request, 'Netflix Account deleted successfully')
        return redirect('accounts')
    else:
        return render(request,"deleteAccount.html")

@login_required(login_url="login")
def renewCustomer(request,pk):
    if request.method=="POST":
        object = get_object_or_404(Customer,id=pk)
        today = date.today()
        nextMonth = today+relativedelta(months=+1)
        object.start_date = today
        object.end_date = nextMonth
        object.save()
        i = Income(amount=object.amount,creation_date=today,netflix_account=object.netflix_account,customer=object)
        i.save()
        messages.success(request,"Congratulations! Customer subscription is renewed sucessfully")
        return redirect('customers')
    else:
        return render(request, 'renewAccounts.html')

@login_required(login_url="login")
def renewNetflix(request,pk):
    if request.method=="POST":
        object = get_object_or_404(Netflix_Account,id=pk)
        today = date.today()
        nextMonth = today+relativedelta(months=+1)
        object.creation_date = today
        object.renewal_date = nextMonth
        object.save()
        e = Expense(card=object.card,amount=object.amount,creation_date=today,netflix_account=object)
        e.save()
        messages.success(request,"Congratulations! Netflix account subscription is renewed sucessfully")
        return redirect('accounts')
    else:
        return render(request, 'renewAccounts.html')
@login_required(login_url="login")
def card(request):
    if request.method == 'POST':
        form = CardForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['card_name']
            number = form.cleaned_data['card_number']
            unique = Card.objects.filter(card_number__exact=number)
            if unique:
                 messages.warning(request, "Card with that number already exists in the system")
            else:
                s = Card(card_name=name,card_number=number)
                s.save()
                messages.success(request,"Superb! Card created successfully")

        else:
            messages.warning(request,form.errors)
            

    all = Card.objects.all()

    n = CardForm()

    context = {
        'cards': all,
        
        'CardForm': n
    }
    return render(request, 'card.html', context)

@login_required(login_url="login")
def editCard(request,pk):
    if request.method == 'POST':
        form = CardForm(request.POST)
        
        if form.is_valid():
            u = Card.objects.get(id=pk)
            u.card_name = form.cleaned_data['card_name']
            u.card_number = form.cleaned_data['card_number']
            u.save()
            messages.success(request,"Superb! Card details updated")
            return redirect('cards')

        else:
            messages.warning(request,form.errors)
    u = get_object_or_404(Card,id=pk)
    form = CardForm()
    form.initial['card_name']= u.card_name
    form.initial['card_number']=u.card_number
    context = {
        'form': form

    }

    return render(request, 'editCard.html', context)

@login_required(login_url="login")
def deleteCard(request,pk):

    if request.method=="POST":
        object = Card.objects.get(id=pk)
        object.delete()
        messages.success(request, 'Card deleted successfully')
        return redirect('cards')
    else:

        return render(request,"deleteAccount.html")

def view_login(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('dashboard')
        else:
            messages.error(request,"Login details are incorrect")
    

    return render(request, "page-login.html")

def logout_view(request):
    logout(request)
    return redirect('login')
