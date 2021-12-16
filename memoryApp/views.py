from django.shortcuts import render,redirect
from django.http import HttpResponse
from memoryApp.models import Memory
from memoryApp.models import Category
import datetime
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.conf import settings

@login_required(login_url = settings.LOGIN_URL)
def memories(request):
    user = request.user
    categories = Category.objects.filter(user = user)
    if categories.count() == 0:
        c1 = Category.objects.create(user=user, categoryName="Family")
        c1.save()
        q1 = Memory.objects.create(title="Family Memories default", description="The most important thing in the world is family and love. Add memories about yours!",
        image = "family.jpeg",category=c1)
        q1.save()
        c2 = Category.objects.create(user=user, categoryName="Friends")
        c2.save()
        q2 = Memory.objects.create(title="Friends Memories default", description="Life is better with friends who become family. Add memories about yours!",
        image = "friends.jpg",category=c2)
        q2.save()
        c3 = Category.objects.create(user=user, categoryName="Personal Milestones")
        c3.save()
        q3 = Memory.objects.create(title="Personal Milestone Memories default", description="Take a glimpse at your success and life milestones. Add memories about yours!",
        image = "personalMileStone.jpg",category=c3)
        q3.save()
    memories = Memory.objects.filter(category__user = user)
    memoriesContext = []
    categorySet = set()
    categories = Category.objects.filter(user = user)
    for memory in memories:
        if memory.category.categoryName not in categorySet:
            categorySet.add(memory.category.categoryName)
            memoriesContext.append(memory)
    context = {
        "categories" : categories,
        "memories" : memoriesContext
    }
    return render(request, "memoryApp/index.html",context )

@login_required(login_url = settings.LOGIN_URL)
def filter(request, cat):
    user = request.user
    memories = Memory.objects.filter(category__categoryName = cat, category__user = user)
    context = {
        "category" : cat,
        "memories" : memories
    }
    return render(request, "memoryApp/gallery.html",context )

@login_required(login_url = settings.LOGIN_URL)
def addCategory(request):
    return render(request, "memoryApp/addCategory.html")

@login_required(login_url = settings.LOGIN_URL)
def addMemory(request,category):
    return render(request, "memoryApp/addMemory.html", {"category":category})

@login_required(login_url = settings.LOGIN_URL)
def add(request, category):
    user = request.user
    title = request.POST["title"]
    location = request.POST["location"]
    description = request.POST["description"]
    date = request.POST["date"]
    Memoryimage = request.FILES["MemoryImage"]
    cat = Category.objects.get(categoryName = category, user = user)
    t = category+" Memories default"
    if Memory.objects.filter(title=t, category=cat).count() == 1:
        Memory.objects.filter(title=t, category=cat).delete()
    memory = Memory.objects.create(title=title, description = description, location= location, datePublished=datetime.datetime.now(),  dateOfOccurence = date, image=Memoryimage, category=cat)
    memory.save()
    return redirect("filter",category)

def addedCategory(request):
    name = request.POST["category"]
    cat = Category.objects.create(user=request.user,categoryName = name)
    cat.save()
    sample_memory = Memory.objects.create(title="Create a memory!",category = cat, image="profile.jpeg")
    sample_memory.save()
    return redirect("memories")
