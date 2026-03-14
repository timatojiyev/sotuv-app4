from django.shortcuts import render
from apps.customer.models import Customer

# Create your views here.


def sotuv_page(request):
    selected_customer = request.GET.get("customer", None)
    customers = Customer.objects.all()
    cart_list = []
    if selected_customer is None:
        first_customer = customers.first()
        if first_customer:
            selected_customer = first_customer.id
            cart_list = first_customer.carts.all()
            selected_cus = first_customer
        else:
            selected_customer = 0
            selected_cus = None
    else:
        selected_cus = Customer.objects.get(id=selected_customer)
        cart_list = selected_cus.carts.all()
    
    context = {
        "customers": customers,
        "selected_customer": int(selected_customer),
        "cart_list": cart_list,
        "total_price": selected_cus.get_cart_total_price() if selected_cus is not None else 0
    }
    return render(request, 'sotuv.html', context=context)

