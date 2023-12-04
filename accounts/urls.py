# accounts/urls.py
from django.urls import path
from .views import SignUpView,EmployerSignUpView,EmployerDashView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("employer/signup", EmployerSignUpView.as_view(),name="empsignup"),
    path("employer/dash", EmployerDashView.as_view(),name="empdash"),
]