from django.shortcuts import render
from apps.customer.models import Customer

# Create your views here.


def sotuv_page(request):
    selected_customer = request.GET.get("customer", None)
    customers = Customer.objects.all()
    if selected_customer is None:
        first_customer = customers.first()
        if first_customer:
            selected_customer = first_customer.id
        else:
            selected_customer = 0
    context = {
        "customers": customers,
        "selected_customer": int(selected_customer)
    }
    return render(request, 'sotuv.html', context=context)

