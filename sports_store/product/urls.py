from django.urls import path
from . import views

app_name = "product"

urlpatterns = [
    path("home_page/", views.home, name="home_page")
]