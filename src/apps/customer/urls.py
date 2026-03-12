from django.urls import path
from . import views


urlpatterns = [
    path('customer-create/', views.customer_create, name="customer_create"),
    path('customer-delete/<int:pk>', views.customer_delete, name="customer_delete"),
]