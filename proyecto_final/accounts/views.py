from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def pagina_principal_accounts(request):
    return HttpResponse("<h1>Pagina principal de accounts</h1>")


def account_login(request):
    return render(request,"accounts/login.html")


def account_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Cuenta creada, bienvenido al blog {username}!")
            return redirect("login")

    else:
        form = UserCreationForm( )

    return render(request,"accounts/register.html", {'form': form} )
    


def account_profile(request):
    return render(request,"accounts/profile.html")
    



