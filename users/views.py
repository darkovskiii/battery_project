from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm
# Create your views here.
# from django.http import HttpResponse
# from django.template import loader


def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, (f"Logged in {user.username}!"))
            return redirect('index')
            # template = loader.get_template('auth/login.html')
            # context = {
            #     'username':username,
            # }
            # return HttpResponse(template.render(context,request))
        else:
            messages.success(
                request, ("There was an error logging in. Try again"))
            return redirect('login')

    else:
        return render(request, "login_user.html", {})


def logout_user(request):
    logout(request)
    messages.success(request, ("Logged out"))
    return redirect('index')


def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, (f"Registration successful {user.username}!"))
            return redirect('index')
    else:
        form = RegisterUserForm()

    return render(request, "register_user.html", {
        "form": form,
    })
