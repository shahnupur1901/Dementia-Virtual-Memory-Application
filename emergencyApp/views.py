from django.shortcuts import render,redirect
from .models import Contact
# Create your views here.
import os
from twilio.rest import Client
from django.contrib import messages
from twilio import twiml
from django.contrib.auth.decorators import login_required
import requests
from django.conf import settings
from aboutMeApp.models import PatientUser
account_sid = ""
auth_token = ""

@login_required(login_url = settings.LOGIN_URL)
def submitContact(request):
    if request.method == 'POST':
        name = request.POST["cname"]
        email = request.POST["email"]
        phonenumber = request.POST["phonenumber"]
        location = request.POST["location"]
        user = request.user
        contact = Contact.objects.create(name = name, email=email, phonenumber=phonenumber, location=location, user = user)
        contact.save()
    return redirect('index')

@login_required(login_url = settings.LOGIN_URL)
def index(request):
    client = Client(account_sid, auth_token)
    contacts = Contact.objects.filter(user = request.user)
    context = {
        "contacts" : contacts,
    }
    return render(request, "emergencyApp/index.html", context)

@login_required(login_url = settings.LOGIN_URL)


def send(request):
    lat = request.POST["latitude"]
    lng = request.POST["longitude"]
    response = requests.get("https://apis.mapmyindia.com/advancedmaps/v1//rev_geocode?lat="+lat+"&lng="+lng)
    data = response.json()
    result = data['results']
    result = result[0]
    address = result['formatted_address']
    context = {
        "address" : address
    }
    return render(request, "emergencyApp/messageBody.html", context)

@login_required(login_url = settings.LOGIN_URL)
def send_msg(request):
    body = request.POST["message"]
    location = request.POST["location"]
    body = "Your patient " +str(PatientUser.objects.get(user = request.user).name)+ " is currently at "+location +" and is in an emergency. He/she sends the message : "+body 
    contacts = Contact.objects.filter(user = request.user)
    
    for contact in contacts:
        client = Client(account_sid, auth_token)
        phno = "+91" + str(contact.phonenumber)
        message = client.messages \
                .create(
                     body=body,
                     from_='+14176402714',
                     to= phno
                 )
       
    messages.success(request, 'Message sent successfully.')
    return redirect("index")

@login_required(login_url = settings.LOGIN_URL)
def contacts(request):
    return render(request, "emergencyApp/contacts.html")

def delContact(request, name):
    Contact.objects.filter(name = name).delete()
    return redirect('index')

def joke(request):
    response = requests.get("https://v2.jokeapi.dev/joke/Programming,Miscellaneous,Pun?blacklistFlags=nsfw,religious,political,racist,sexist,explicit&type=single")
    data = response.json()
    context = {
        "joke" : data["joke"]
    }


    return render(request, "emergencyApp/joke.html",context)