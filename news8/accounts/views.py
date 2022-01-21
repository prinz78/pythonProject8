from django.shortcuts import render
from .forms import CustomUserCreationForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

# Create your views here.

class SignupPageView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
