from django.shortcuts import render
from django .views import generic
from django.urls import reverse_lazy
from .forms import SignUpForm, EditForm, PasswordChangingForm
from django.contrib.auth.views import PasswordChangeView

class UserRegister(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class UserEdit(generic.UpdateView):
    form_class = EditForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('/')

    def get_object(self):
        return self.request.user

class PasswordsChange(PasswordChangeView):
    form_class = PasswordChangingForm
    success_url = reverse_lazy('password_success')

def password_success(request):
        return render(request, 'registration/password_success.html', {})