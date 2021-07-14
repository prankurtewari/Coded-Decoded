from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

# Create your views here.

class UserRegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


# from django.shortcuts import render, redirect
# from django.contrib import messages
# from django.contrib.auth import authenticate, login, logout
# from .forms import UserRegisterForm

# # Create your views here.
# def register(request):
#     if request.method == 'POST':
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request, f'Account Created for {username}!')
#             return redirect('login')
#     else:
#         form = UserRegisterForm()
#     return render(request, 'authenticate/register.html', {'form': form})




# second way without loginview
# def Userlogin(request):
#     if request.method == 'POST':
#         form = UserLoginForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     messages.success(
#                         request, f'Succesfully logged in for {username}!')
#                     return redirect('register')
#                 else:
#                     messages.success(
#                         request, f'Succesfully disabled in for {username}!')
#                     return redirect('logout')
#             else:
#                 return redirect('login')
#     else:
#         form = UserLoginForm()
#     return render(request, 'authenticate/login.html', {'form': form})
