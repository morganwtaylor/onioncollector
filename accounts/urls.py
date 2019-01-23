from django.urls import path, include

from . import views

app_name="accounts"

urlpatterns = [
    path("signup/", views.SignupView.as_view(), name='signup'),
    path("logout/", views.LogoutView.as_view(), name='logout'),
    path("login/", views.LoginView.as_view(), name='login'),
]
