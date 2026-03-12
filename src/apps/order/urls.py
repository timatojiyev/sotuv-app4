from django.urls import path
from . import views


urlpatterns = [
    path('sotuv-page/', views.sotuv_page, name="sotuv_page"),
]