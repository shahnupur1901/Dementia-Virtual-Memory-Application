from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from memoryApp.models import Memory, Category
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from memoryApp.models import Category
#from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def loginpage(request):
    if request.method== "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username = username, password=password)
        if user is not None :
            login(request, user)
            #Create 3 predefined category instances 
            return redirect("home")
        else :
            return redirect("login")


    context = {}
    return render(request, "accounts/login.html", context)




def registerpage(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    context = {
        "form": form
    }
    return render(request, "accounts/r.html", context)



def logoutPage(request):
    logout(request)
    return redirect("login")

#@login_required(login_url = "login")
def home(request):
    return render(request, "accounts/home.html")

def contact(request):
    return render(request,"accounts/contact.html")