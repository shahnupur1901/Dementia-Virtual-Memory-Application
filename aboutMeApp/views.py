from django.shortcuts import render,redirect
from .models import PatientUser
from django.conf import settings
# Create your views here.
from django.contrib.auth.decorators import login_required
@login_required(login_url = settings.LOGIN_URL)
def aboutMe(request):
    try:
        profile = PatientUser.objects.get(user = request.user)
    except PatientUser.DoesNotExist:
        profile = PatientUser.objects.create(user=request.user, name="Create your profile!",profilePicture="profile.jpeg")
        profile.save()
    context = {
        "profile":profile,
    }
    return render(request,"aboutMeApp/index.html",context)

@login_required(login_url = settings.LOGIN_URL)
def editProfile(request):
    profile = PatientUser.objects.get(user = request.user)
    return render(request,"aboutMeApp/editProfile.html",{"profile":profile})

@login_required(login_url = settings.LOGIN_URL)    
def submit(request):
    profile = PatientUser.objects.get(user = request.user)
    profile.name = request.POST["name"]
    profile.profilePicture = request.FILES["profileImage"]
    profile.description = request.POST["description"]
    profile.birthdate = request.POST["birthdate"]
    profile.save()
    return redirect("aboutMe")
