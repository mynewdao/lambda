from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.urls import reverse

User = get_user_model()


class CreateUserView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'accounts/register.html'
    model = User

    def get_success_url(self):
        return reverse('login')
