from django.shortcuts import render, redirect
from .models import Category, Product
# Create your views here.


def monitoring_page(request):
    return render(request, "monitoring.html")


def products_page(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, "products.html", context=context)


def products_create_page(request):
    if request.method == 'POST':
        image_file = request.FILES.get("image") 
        data = request.POST            
        product_name = data.get("product_name")
        product_barcode = data.get("product_barcode")
        product_category = data.get("product_category")
        input_price = data.get("input_price")
        current_price = data.get("current_price")
        wholesale_price = data.get("wholesale_price")
        qoldiq = data.get("qoldiq")
        min_qoldiq = data.get("min_qoldiq")
        status = data.get("status")
        try:
            category = Category.objects.get(id=product_category)
            product = Product.objects.create(
                category = category, 
                name = product_name,
                image = image_file,
                barcode = product_barcode,
                input_price = input_price,
                current_price = current_price,
                wholesale_price = wholesale_price,
                qoldiq = qoldiq,
                min_qoldiq = min_qoldiq,
                is_active = True if status == "on" else False
            )
            print(product)
        except Category.DoesNotExist:
            msg = "Category yoq yoki tanlanmadi!"
        return redirect("products_page")
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, "products-create.html", context=context)