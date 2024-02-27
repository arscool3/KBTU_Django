from django.shortcuts import render, redirect
from .models import Airplane, Consumer, Ticket
from .forms import *


def get_by_phone_number(request, phone_number):
    consumers_by_phone = Consumer.objects.get_by_phone_number(phone_number)
    return render(request, 'consumers_by_phone.html', {'phone': phone_number, 'consumers': consumers_by_phone})


def get_by_email(request, email):
    consumers_by_email = Consumer.objects.get_by_email(email)
    return render(request, 'consumers_by_email.html', {'email':email, 'consumers': consumers_by_email})


def get_active_airplanes(request):
    active_airplanes = Airplane.objects.get_active_airplanes()
    return render(request, 'active_airplanes.html', {'active_airplanes': active_airplanes})


def get_inactive_airplanes(request):
    inactive_airplanes = Airplane.objects.get_inactive_airplanes()
    return render(request, 'inactive_airplanes.html', {'inactive_airplanes': inactive_airplanes})


def create_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)

        if form.is_valid():
            new_ticket = form.save()
            return render(request, 'ticket_created.html', {'ticket': new_ticket})
    else:
        form = TicketForm()

    return render(request, 'create_ticket.html', {'form': form})

def create_airplane(request):
    if request.method == 'POST':
        form = AirplaneForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('active_airplanes')
    else:
        form = AirplaneForm()

    return render(request, 'create_airplane.html', {'form': form})


def create_consumer(request):
    if request.method == 'POST':
        form = ConsumerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_active_airplanes')
    else:
        form = ConsumerForm()

    return render(request, 'create_consumer.html', {'form': form})

