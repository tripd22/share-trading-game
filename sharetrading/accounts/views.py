# accounts/views.py
from django.urls import reverse_lazy
from django.views import generic

from users.forms import CustomUserCreationForm

class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
