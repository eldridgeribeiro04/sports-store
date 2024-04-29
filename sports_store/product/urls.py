from django.urls import path
from . import views

app_name = "product"

urlpatterns = [
    # path("categories/", views.category_view, name='categories'),
    path("items/<int:brand_id>/", views.items, name="items"),
    path("single/<int:item_id>/", views.item_view, name="single"),
]