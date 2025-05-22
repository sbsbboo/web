from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from userauth.forms import login_form, register_form

def register_view(request):
    form = register_form(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        messages.success(request, 'Account created successfully!')
        return redirect('login')
    return render(request, 'register.html', {'form': form})

def login_view(request):
    form = login_form(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(request, username=username, password=password)
        
        if user:
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect('test')  # redirect to index page
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html', {'form': form})

@login_required
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, "You have been logged out.")
        return redirect('home') 
    else:
        return render(request, 'index.html', {'user': request.user}) 

@login_required
def index_view(request):
    return render(request, 'index.html', {'user': request.user})



#self code
def home_view(request):
    return render(request, 'home.html')

def test_view(request):
    return render(request, 'test.html')

def forgetpwd_view(request):
    return render(request, 'forgetpwd.html')