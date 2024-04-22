from django.urls import path

from .views import SignUpView, ProfileUpdateView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("update/<int:pk>/", ProfileUpdateView.as_view(), name='update'),
]