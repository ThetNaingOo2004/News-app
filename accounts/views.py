from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCerationForm
from django.contrib.auth import views as auth_views



# Create your views here.

class SignUpView(CreateView):
    form_class = CustomUserCerationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


