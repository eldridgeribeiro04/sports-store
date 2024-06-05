from django.urls import path
from store.api import views

urlpatterns = [
    path('items/', views.ItemViewMVS.as_view(), name='items'),
]