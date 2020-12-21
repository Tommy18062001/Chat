from django.shortcuts import render, redirect
from .forms import CreateUSerForm


# i need a message to say to the user if the account was created or not, django offer one function for that
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.

from django.views.decorators.csrf import csrf_exempt

# it can be possible to go the home even though you didn't login yet, that's totally weird. let's change that
from django.contrib.auth.decorators import login_required


# be careful when you use this, don't put it everywhere
@ login_required(login_url='login')
def home(request):
    return render(request, "Account/home.html", {})


@ csrf_exempt
def loginPage(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        # now, let's use our authenticate. this is another one. really i don't how to use this as well
        user = authenticate(request, username=username, password=password)

        # maybe, it's for checking that the user is not None
        if user is not None:
            login(request, user=user)
            return redirect("accounts:home")
        else:
            messages.info(request, 'Username or Password is incorrect')

    context = {}
    # don't never forget to put return, hahaha
    return render(request, "Account/login.html", context)


@ csrf_exempt
def logoutPage(request):
    logout(request)
    return redirect('accounts:login')


@ csrf_exempt
def register(request):
    form = CreateUSerForm()
    if request.method == "POST":
        form = CreateUSerForm(request.POST)

        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('accounts:login')

    context = {"form": form}
    return render(request, "Account/register.html", context)





