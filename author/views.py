from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from . import forms
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from album.models import Album
from django.contrib.auth.views import LoginView,LogoutView
# Create your views here.

def register(request):
    if request.method == 'POST':
        register_form = forms.RegistrationForm(request.POST)
        if register_form.is_valid():
            messages.success(request, 'Account created Successfully')
            register_form.save()
            return redirect('register')
    else:
        register_form = forms.RegistrationForm()
    return render(request, 'register.html', {'form': register_form, 'type': 'Register'})

    

class UserLoginView(LoginView):
    template_name = 'register.html'
    
    def get_success_url(self):
        return reverse_lazy('profile')

    def form_valid(self, form):
        messages.success(self.request, 'Logged in Successful')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.success(self.request, 'Logged in information incorrect')
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context
    
    
    
    

@login_required
def profile(request):
    data = Album.objects.all()
    return render(request, 'profile.html',{'dataAlbum':data,'type': 'Profile Page'})

class UserLogoutView(LogoutView):
     def get_success_url(self):
        return reverse_lazy('login')

