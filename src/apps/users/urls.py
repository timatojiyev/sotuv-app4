from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard_page, name="dashboard_page"),
    path("auth/login/", views.login_page, name="login_page"),
    path("logout/", views.login_page, name="login_page"),
]
