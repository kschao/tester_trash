from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse
from django.shortcuts import render
from .models import Customer
# Create your views here.

# TODO: Create a function for each path created in customers/urls.py. Each will need a template as well.

def index(request):
    # The following line will get the logged-in in user (if there is one) within any view function
    user = request.user

    try:
        # This line inside the 'try' will return the customer record of the logged-in user if one exists
        log_in_customer = Customer.objects.get(user=user)
    except:
        return HttpResponseRedirect(reverse('customers:create'))
        print(user)
        # TODO: Redirect the user to a 'create' function to finish the registration process if no customer record found
        pass
def create(request):
    if request.method == 'POST':
        user = request.user
        name = request.POST.get('name')
        pickup_day = request.POST.get('pickup_day')
        address = request.POST.get('address')
        zipcode = request.POST.get('zipcode')
        new_customer = Customer(name=name, user=user, pickup_day=pickup_day, address=address, zipcode=zipcode)
        new_customer.save()
        return HttpResponseRedirect(reverse('customers:index'))
    else:
        return render(request, 'customers/create.html')
    # It will be necessary while creating a Customer/Employee to assign request.user as the user foreign key
def change(request):
    if request.method == "POST":
        user = request.user
        log_in_customer = Customer.objects.get(user=user)
        log_in_customer.pickup_day = request.POST.get('pickup_day')
        log_in_customer.onetime_pickup = request.POST.get('onetime_pickup')
        log_in_customer.suspend_start = request.POST.get('suspend_start')
        log_in_customer.suspend_end = request.POST.get('suspend_end')
        log_in_customer.save()
        return HttpResponseRedirect(reverse('customers:index'))
    else:
        user = request.user
        customer_edit = Customer.objects.get(user=user)
        context = {
            'customers': customer_edit
    }
        return render(request, 'customers/change.html', context)

def account(request):
    user = request.user
    log_in_customer = Customer.objects.get(user=user)
    context = {
        'log_in_customer': log_in_customer
    }
    return render(request, 'customers/account.html', context)
