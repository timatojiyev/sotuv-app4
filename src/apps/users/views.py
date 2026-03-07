from django.shortcuts import render, redirect

# Create your views here.

def dashboard_page(request):

    if not request.user.is_authenticated:
        return redirect("login_page")

    return render(request, "dashboard.html")


def login_page(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username, password)
    
    return render(request, "login.html")
