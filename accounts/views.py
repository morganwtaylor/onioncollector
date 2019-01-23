from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy #redirect once form is submitted
from django.views import generic
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, Http404, JsonResponse

from . import forms

########## LOGIN, SIGNUP, LOGOUT #############
class LoginView(generic.FormView):
    form_class = AuthenticationForm
    success_url = reverse_lazy("home")
    template_name ='accounts/login.html'

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        return form_class(self.request, **self.get_form_kwargs()) #returns form with fields passed

    def form_valid(self, form): # They submitted succesffully and the user is legit then...
        login(self.request, form.get_user()) #processing information and returns info for authenticated user.
        return super().form_valid(form)


class LogoutView(generic.RedirectView): #simple log out view
    url = reverse_lazy("home")

    def get(self, request, *args, **kwargs):
        logout(request)
        return super().get(request, *args, **kwargs)


class SignupView(generic.CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("accounts:login")
    template_name = 'accounts/signup.html'
