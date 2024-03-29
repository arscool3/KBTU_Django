from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Event, Participant, Organizer, Ticket, Sponsor, Profile
from django.contrib.auth.models import User
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.decorators import method_decorator
import json
from django.contrib.auth.views import LoginView, LogoutView
from .forms import CustomUserCreationForm
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, decorators, logout, forms



def basic_form(request, given_form):
    if request.method == 'POST':
        form = given_form(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("OK")
        else:
            raise Exception(f"some erros {form.errors}")
    return render(request, 'index.html', {'form': given_form()})

def register_view(request):
    return basic_form(request, forms.UserCreationForm)



def logout_view(request):
    logout(request)
    return HttpResponse("You have logout")


def login_view(request):
    if request.method == 'POST':
        form = forms.AuthenticationForm(data=request.POST)
        if form.is_valid():
            try:
                user = authenticate(**form.cleaned_data)
                login(request, user)
                if next := request.GET.get("next"):
                    return redirect(next)
                return HttpResponse("everything is ok")
            except Exception:
                return HttpResponse("something is not ok")
        else:
            raise Exception(f"some erros {form.errors}")
    return render(request, 'index.html', {'form': forms.AuthenticationForm()})




@require_http_methods(["GET"])
def get_events(request):
    events = Event.objects.all()
    return render(request, 'home.html', {'events': events})


@require_http_methods(["GET"])
def get_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    return render(request, 'event_detail.html', {'event': event})


@method_decorator(login_required(login_url='/accounts/login/'), name='dispatch')
@require_http_methods(["GET"])
def get_event_participants(request, event_id):
    participants = Participant.objects.filter(event_id=event_id).values()
    return render(request, 'participant_list.html', {'participants': participants})


@method_decorator(login_required(login_url='/accounts/login/'), name='dispatch')
@require_http_methods(["GET"])
def get_user_tickets(request, user_id):
    tickets = Ticket.objects.filter(purchaser_id=user_id).values()
    return JsonResponse(list(tickets), safe=False)


@method_decorator(login_required(login_url='/accounts/login/'), name='dispatch')
@require_http_methods(["GET"])
def get_user_profile(request, user_id):
    profile = get_object_or_404(Profile, user_id=user_id)
    return JsonResponse({'bio': profile.bio, 'avatar': profile.avatar.url})


@method_decorator(login_required(login_url='/accounts/login/'), name='dispatch')
@require_http_methods(["GET"])
def get_event_sponsors(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    sponsors = event.sponsor_set.all().values()
    return JsonResponse(list(sponsors), safe=False)



@method_decorator(login_required(login_url='/accounts/login/'), name='dispatch')
@csrf_exempt
@require_http_methods(["POST"])
def create_event(request):
    try:
        data = json.loads(request.body)
        event = Event(title=data['name'], description=data['about'], date=data['date'])
        event.save()
        return JsonResponse({'id': event.id, 'name': event.name, 'about': event.about, 'date': event.date}, status=201)
    except (ValueError, KeyError) as e:
        return JsonResponse({'error': str(e)}, status=400)


@method_decorator(login_required(login_url='/accounts/login/'), name='dispatch')
@csrf_exempt
@require_http_methods(["POST"])
def register_participant(request, event_id):
    try:
        user_id = json.loads(request.body)['user_id']
        user = User.objects.get(pk=user_id)
        event = Event.objects.get(pk=event_id)
        participant = Participant(user=user, event=event)
        participant.save()
        return JsonResponse({'id': participant.id, 'user': participant.user.id, 'event': participant.event.id, 'joined_at': participant.joined_at}, status=201)
    except (User.DoesNotExist, Event.DoesNotExist, ValueError, KeyError) as e:
        return JsonResponse({'error': str(e)}, status=400)


@method_decorator(login_required(login_url='/accounts/login/'), name='dispatch')
@csrf_exempt
@require_http_methods(["POST"])
def create_organizer(request):
    try:
        data = json.loads(request.body)
        user = User.objects.get(pk=data['user_id'])
        organizer = Organizer(user=user, organization_name=data['organization_name'])
        organizer.save()
        return JsonResponse({'id': organizer.id, 'user': organizer.user.id, 'organization_name': organizer.organization_name}, status=201)
    except (User.DoesNotExist, ValueError, KeyError) as e:
        return JsonResponse({'error': str(e)}, status=400)


@method_decorator(login_required(login_url='/accounts/login/'), name='dispatch')
@csrf_exempt
@require_http_methods(["POST"])
def purchase_ticket(request, event_id):
    try:
        user_id = json.loads(request.body)['user_id']
        user = User.objects.get(pk=user_id)
        event = Event.objects.get(pk=event_id)
        ticket = Ticket(event=event, purchaser=user, purchase_date=timezone.now())
        ticket.save()
        return JsonResponse({'id': ticket.id, 'event': ticket.event.id, 'purchaser': ticket.purchaser.id, 'purchase_date': ticket.purchase_date}, status=201)
    except (User.DoesNotExist, Event.DoesNotExist, ValueError, KeyError) as e:
        return JsonResponse({'error': str(e)}, status=400)


@method_decorator(login_required(login_url='/accounts/login/'), name='dispatch')
@csrf_exempt
@require_http_methods(["POST"])
def add_sponsor(request, event_id):
    try:
        name = json.loads(request.body)['name']
        event = Event.objects.get(pk=event_id)
        sponsor = Sponsor(name=name)
        sponsor.save()
        sponsor.event.add(event)
        return JsonResponse({'id': sponsor.id, 'name': sponsor.name}, status=201)
    except (Event.DoesNotExist, ValueError, KeyError) as e:
        return JsonResponse({'error': str(e)}, status=400)


@method_decorator(login_required(login_url='/accounts/login/'), name='dispatch')
@csrf_exempt
@require_http_methods(["POST"])
def update_profile(request, user_id):
    try:
        data = json.loads(request.body)
        profile = Profile.objects.get(user_id=user_id)
        profile.bio = data.get('bio', profile.bio)
        if 'avatar' in request.FILES:
            profile.avatar = request.FILES['avatar']
        profile.save()
        return JsonResponse({'id': profile.id, 'user': profile.user.id, 'bio': profile.bio, 'avatar': profile.avatar.url}, status=200)
    except (Profile.DoesNotExist, ValueError, KeyError) as e:
        return JsonResponse({'error': str(e)}, status=400)