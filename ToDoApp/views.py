from django.shortcuts import render,redirect

from . models import Note
# Create your views here.
def toDoApp(request):
    notes = Note.objects.filter(user=request.user)
    context={
        "notes":notes
    }

    return render(request, "ToDoApp/index.html",context)

def addnote(request):
        desc=request.POST["note"]
        note=Note.objects.create(user=request.user,description=desc)
        return redirect("ToDoApp")

def delnote(request, uid):
        Note.objects.get(user = request.user, uid = uid).delete()
        return redirect("ToDoApp")
