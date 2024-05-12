from django.shortcuts import render,HttpResponse,redirect
from django.template import loader
from .forms import RoomForm, EquipmentForm,UsageForm
from .models import Room,Equipment,Usage


def RoomView(request):
    if request.method == "POST" :
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
    context = {}
    context['form'] = RoomForm()
    context['table'] = Room.objects.all()
    return render(request,"room.html",context)

def DeleteRoomView(request):
    Room.objects.filter(id = request.POST.get("id")).delete()
    return redirect("rooms")

def EqView(request):
    if request.method == "POST" :
        form = EquipmentForm(request.POST)
        if form.is_valid():
            form.save()
    context = {}
    context['form'] = EquipmentForm()
    context['table'] = Equipment.objects.all()
    return render(request,"eq.html",context)


def UsageView(request):
    if request.method == "POST" :
        form = UsageForm(request.POST)
        if form.is_valid():
            form.save()
    context = {}
    context['form'] = UsageForm()
    context['table'] = Usage.objects.all()
    return render(request,"usage.html",context)



