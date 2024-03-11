from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Event,Schedule,Ticket,Organizer
from django.contrib.auth import authenticate, login, decorators, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import OrganizerSignUpForm, EventForm, TicketForm, ScheduleForm, AttendeeForm



# GET ENDPOINTS
@decorators.login_required(login_url='signin')
def event_list(request):
    events = Event.objects.all()
    return render(request, 'get/event_list.html', {"events" : events})

@decorators.login_required(login_url='signin')
def event_detail(request, event_id):
    event = Event.objects.get(id = event_id)
    return render(request, 'get/event_detail.html', {"event" : event})

@decorators.login_required(login_url='signin')
def attendee_list(request, event_id):
    event = Event.objects.get(id = event_id)
    tickets = Ticket.objects.filter(event=event)
    attendees = [ticket.attendee for ticket in tickets]
    return render(request, 'get/attendee_list.html', {"event" : event, "attendees" : attendees})

@decorators.login_required(login_url='signin')
def event_schedule(request, event_id):
    event = Event.objects.get(id = event_id)
    schedule = Schedule.objects.get(event = event)

    return render(request, 'get/schedule.html', {"schedule" : schedule})

@decorators.login_required(login_url='signin')
def ticket_list(request):
    tickets = Ticket.objects.all()

    return render(request, 'get/ticket_list.html', {"tickets": tickets})

@decorators.login_required(login_url='signin')
def ticket_detail(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)

    return render(request, 'get/ticket_detail.html', {"ticket":ticket})
##################


# POST ENDPOINTS
def signup(request):
    if request.method == 'POST':
        form = OrganizerSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('event_list')
    else:
        form = OrganizerSignUpForm()
    return render(request, 'post/signup.html', {'form': form})

def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('event_list')  
    else:
        form = AuthenticationForm()
    return render(request, 'post/signin.html', {'form': form})

def signout(request):
    logout(request)
    return redirect('signin')

@decorators.login_required(login_url='signin')
def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid:
            event = form.save(commit=False)
            organizer = Organizer.objects.get(user=request.user)
            event.organizer = organizer
            event.save()
            return redirect('event_list')
    else:
        form = EventForm()

    return render(request, 'post/create_event.html', {"form" : form})

@decorators.login_required(login_url='signin')
def event_delete(request, event_id):
    event = Event.objects.get(id = event_id)
    if event.organizer.user == request.user or request.user.is_superuser:
        event.delete()
        return redirect('event_list')
    else:
        return render(request, 'error.html', {'message': 'You are not authorized to delete this event.'})

@decorators.login_required(login_url='signin')
def schedule_create(request, event_id):
    event = Event.objects.get(id = event_id)
    if event.organizer.user == request.user or request.user.is_superuser:
        if request.method == 'POST':
            form = ScheduleForm(request.POST)
            if form.is_valid():
                schedule = form.save(commit=False)
                schedule.event = event
                schedule.save()
                return redirect('event_list')
        else:
            form = ScheduleForm()

        return render(request, 'post/create_schedule.html', {'form': form})
    else:
        return render(request, 'error.html', {'message': 'You are not authorized to create schedule for this event.'})

@decorators.login_required(login_url='signin')
def ticket_create(request, event_id):
    event = Event.objects.get(id=event_id)
    if event.organizer.user == request.user or request.user.is_superuser:
        if request.method == 'POST':
            form = TicketForm(request.POST)
            if form.is_valid(): 
                ticket = form.save(commit=False)
                ticket.event = event
                ticket.save()
                return redirect('ticket_list')
        else:
            form = TicketForm()

        return render(request, 'post/create_ticket.html', {'form': form})
    else:
        return render(request, 'error.html', {'message': 'You are not authorized to create a ticket for this event.'})

@decorators.login_required(login_url='signin')
def create_attendee(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = AttendeeForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('event_list')
        else:
            form = AttendeeForm()

        return render(request, 'post/create_attendee.html', {'form': form})
    else:
        return render(request, 'error.html', {'message': 'You are not authorized to create a attendee.'})
################

        
@decorators.login_required(login_url='signin')
def event_by_organizer(request, name):
    organizer = Organizer.objects.get(name=name)
    events = Event.objects.get_events_by_organizer(organizer)

    return render(request, 'manager/event_by_organizer.html', {"events": events, "organizer" : organizer})


@decorators.login_required(login_url='signin')
def tickets_by_event(request, event_id):
    event = Event.objects.get(id=event_id)

    tickets = Ticket.objects.get_tickets_by_event(event)

    return render(request, 'manager/tickets_by_event.html', {"event": event, "tickets" : tickets})

