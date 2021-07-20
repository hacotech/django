from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContactForm, LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, get_user_model


def home_page(request):
    print(f"is Authenticated: {request.user.is_authenticated}")
    context = {
        'title': 'Home Page'
    }
    return render(request, "home_page.html", context)


def about_page(request):
    context = {
        'title': 'About Us Page'
    }
    return render(request, "about_page.html", context)


def contact_page(request):
    form = ContactForm(request.POST or None)
    context = {
        'title': 'Contact Us Page',
        'form': form
    }

    if form.is_valid():
        print(form.cleaned_data)

    return render(request, "contact_page.html", context)


def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        'title': 'Login',
        'form': form
    }
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            print('Error')
    return render(request, "login_page.html", context)


User = get_user_model()


def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        'title': 'Register',
        'form': form
    }
    if form.is_valid():
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        new_user = User.objects.create_user(username=username, email=email, password=password)
        print(new_user)
    return render(request, "register_page.html", context)
