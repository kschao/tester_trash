from .models import Employees
from django.shortcuts import reverse
from datetime import datetime as dt
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.apps import apps

# Create your views here.

# TODO: Create a function for each path created in employees/urls.py. Each will need a template as well.


def index(request):
    user = request.user
    # This line will get the Customer model from the other app, it can now be used to query the db for Customers
    Customer = apps.get_model('customers.Customer')
    customers = Customer.objects.all()
    now = dt.now
    today = now.strftime('%A')
    try:
        log_in_employee = Employees.objects.get(user=user)
    except: 
        return HttpResponseRedirect(reverse('employees:create'))
    occurring_customers = []
    for customer in customers:
        if customer.zipcode == log_in_employee.zipcode:
            occurring_customers.append(customer.name)
    context = {
        'log_in_employee': log_in_employee,
        'customers': occurring_customers,
        'customers_address': customer.address
        }
    print(occurring_customers)
    return render(request, 'employees/index.html', context)

def create(request):
    if request.method == "POST":
        user = request.user
        name = request.POST.get('name')
        zipcode = request.POST.get('zipcode')
        new_employee = Employees(name=name, user=user, zipcode=zipcode)
        new_employee.save()
        return HttpResponseRedirect(reverse('employees/create.html'))
    else:
        return render(request, 'employees/create.html')

def account(request):
    user = request.user
    log_in_employees = Employees.objects.get(user=user)
    context = {
        'log_in_customer': log_in_employees
    }
    return render(request, 'customers/account.html', context)    

def change(request):
    if request.method == "POST":
        user = request.user
        log_in_employees = Employees.objects.get(user=user)
        log_in_employees.pickup_day = request.POST.get('pickup_day')
        log_in_employees.onetime_pickup = request.POST.get('onetime_pickup')
        log_in_employees.suspend_start = request.POST.get('suspend_start')
        log_in_employees.suspend_end = request.POST.get('suspend_end')
        log_in_employees.save()
        return HttpResponseRedirect(reverse('customers:index'))
    else:
        user = request.user
        customer_edit = Employees.objects.get(user=user)
        context = {
            'customers': customer_edit
    }
        return render(request, 'customers/change.html', context)