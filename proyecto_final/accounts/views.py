from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def pagina_principal_accounts(request):
    return HttpResponse("<h1>Pagina principal de accounts</h1>")


def account_login(request):
    return render(request,"accounts/login.html")

def account_register(request):
    return render(request,"accounts/register.html")
    
def account_profile(request):
    return render(request,"accounts/profile.html")
    