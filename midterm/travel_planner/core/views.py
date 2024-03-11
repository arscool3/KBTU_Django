from django.shortcuts import render
from django.shortcuts import redirect
from django.http import JsonResponse
from datetime import datetime
import json
from .models import Ticket, Accommodation, Place
from rest_framework import generics
from .serializers import TicketSerializer, AccommodationSerializer, PlaceSerializer

class PlaceAPIView(generics.ListCreateAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
 

class PlaceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer

class TicketAPIView(generics.ListCreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

class TicketDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

class AccommodationAPIView(generics.ListCreateAPIView):
    queryset = Accommodation.objects.all()
    serializer_class = AccommodationSerializer

class AccommodationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Accommodation.objects.all()
    serializer_class = AccommodationSerializer


def home(request):
    message = request.session.pop('message', None)
    return render(request, 'home.html',  {'message': message})


def ticket_search(request):
    cities = Place.objects.all()
    if request.method == 'GET':
        return render(request, 'ticket_search.html', {'cities': cities})
    elif request.method == 'POST':
        departure = request.POST.get('departure')
        destination = request.POST.get('destination')
        date = request.POST.get('date')
        travelers = int(request.POST.get('travelers'))
        request.session['travelers'] = travelers
        tickets = Ticket.objects.filter(departure_city=departure, destination_city=destination, date=date)
        if not tickets:
            message = "No tickets available for the selected destination and date."
            return render(request, 'ticket_search.html', {'message': message, 'cities': cities})
        
        cheapest_ticket = min(tickets, key=lambda x: x.price) 
        for ticket in tickets:
            ticket.cheapest = (ticket == cheapest_ticket)
        return render(request, 'ticket_search.html', {'tickets': tickets, 'cheapest_ticket': cheapest_ticket, 'cities': cities, 'departure': departure, 'destination': destination, 'date': date, 'travelers': travelers})


def add_ticket_to_cart(request, ticket_id):
    if request.method == 'POST':
        travelers = request.session.pop('travelers', None)
        ticket_info = {'ticket_id': ticket_id, 'travelers': travelers}  
        if 'cart' not in request.session:
            request.session['cart'] = {'tickets': [ticket_info], 'accommodations': []}
        else:
            request.session['cart']['tickets'].append(ticket_info)
        request.session['message'] = "Ticket successfully added to cart!"
        return redirect('home')
    else:
        return redirect('home')

    
def accommodation_search(request):
    cities = Place.objects.all()
    if request.method == 'GET':
        return render(request, 'accommodation_search.html', {'cities': cities})
    elif request.method == 'POST':
        destination = request.POST.get('destination')
        arrival_date = request.POST.get('arrival_date')
        departure_date = request.POST.get('departure_date')
        request.session['num_nights'] = (datetime.strptime(departure_date, '%Y-%m-%d') - datetime.strptime(arrival_date, '%Y-%m-%d')).days
        visitors = int(request.POST.get('visitors'))
        request.session['visitors'] = visitors
        accommodations = Accommodation.objects.filter(destination_city=destination)
        if not accommodations:
            message = "No accommodations available for the selected city and dates."
            return render(request, 'accommodation_search.html', {'message': message, 'cities': cities})
        cheapest_accommodation = min(accommodations, key=lambda x: x.price_per_night) 
        for accommodation in accommodations:
            accommodation.cheapest = (accommodation == cheapest_accommodation)
        message = request.session.pop('message', None)
        return render(request, 'accommodation_search.html', {'accommodations': accommodations, 'cheapest_accommodation': cheapest_accommodation, 'message': message, 'cities': cities, 'destination': destination, 'arrival_date': arrival_date, 'departure_date': departure_date, 'visitors': visitors})


def add_accommodation_to_cart(request, accommodation_id):
    if request.method == 'POST':
        visitors = request.session.pop('visitors', None)
        num_nights = request.session.pop('num_nights', None)
        accommodation_info = {'accommodation_id': accommodation_id, 'visitors': visitors, 'num_nights': num_nights} 
        if 'cart' not in request.session:
            request.session['cart'] = {'tickets': [], 'accommodations': [accommodation_info]}
        else:
            request.session['cart']['accommodations'].append(accommodation_info)
        request.session['message'] = "Accommodation successfully added to cart!"
        return redirect('home')
    else:
        return redirect('home')


def view_cart(request):
    if 'cart' in request.session:
        ticket_ids = [item['ticket_id'] for item in request.session.get('cart', {}).get('tickets', [])]
        accommodation_ids = [item['accommodation_id'] for item in request.session.get('cart', {}).get('accommodations', [])]

        ticket_items = Ticket.objects.filter(id__in=ticket_ids)
        ticket_travelers = [item['travelers'] for item in request.session.get('cart', {}).get('tickets', [])]
        for ticket, travelers in zip(ticket_items, ticket_travelers):
            ticket.travelers = travelers

        accommodation_items = Accommodation.objects.filter(id__in=accommodation_ids)

        accommodation_visitors = [item['visitors'] for item in request.session.get('cart', {}).get('accommodations', [])]
        accommodation_nights = [item['num_nights'] for item in request.session.get('cart', {}).get('accommodations', [])]
        for accommodation, visitors, nights in zip(accommodation_items, accommodation_visitors, accommodation_nights):
            accommodation.visitors = visitors
            accommodation.num_nights = nights
        
        for ticket in ticket_items:
            ticket.total_price = ticket.price * ticket.travelers
        for accommodation in accommodation_items:
            accommodation.total_price = accommodation.price_per_night * accommodation.visitors *  accommodation.num_nights
        total_price = sum(ticket.total_price for ticket in ticket_items)
        total_price += sum(accommodation.total_price for accommodation in accommodation_items)

        return render(request, 'cart.html', {'ticket_items': ticket_items, 'accommodation_items': accommodation_items, 'total_price': total_price})
    else:
        #message = "Your cart is empty."
        return render(request, 'cart.html')


def delete_ticket_from_cart(request):
    if request.method == 'POST':
        ticket_id = int(request.POST.get('ticket_id'))
        if 'cart' in request.session:
            cart = request.session['cart']
            for item in cart['tickets']:
                if item['ticket_id'] == ticket_id:
                    cart['tickets'].remove(item)
                    request.session['cart'] = cart
                    return redirect('cart')
        


def delete_accommodation_from_cart(request):
    if request.method == 'POST':
        accommodation_id = int(request.POST.get('accommodation_id'))
        if 'cart' in request.session:
            cart = request.session['cart']
            for item in cart['accommodations']:
                if item['accommodation_id'] == accommodation_id:
                    cart['accommodations'].remove(item)
                    request.session['cart'] = cart
                    return redirect('cart')
        

def update_ticket_quantity(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        ticket_id = int(data.get('ticket_id'))
        travelers = int(data.get('travelers'))

        if 'cart' in request.session:
            cart = request.session['cart']
            for item in cart['tickets']:
                if item['ticket_id'] == ticket_id:
                    item['travelers'] = travelers
                    request.session['cart'] = cart
                    return redirect('cart')


def update_accommodation_quantity(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        accommodation_id = int(data.get('accommodation_id'))
        visitors = int(data.get('visitors'))

        if 'cart' in request.session:
            cart = request.session['cart']
            for item in cart['accommodations']:
                if item['accommodation_id'] == accommodation_id:
                    item['visitors'] = visitors
                    request.session['cart'] = cart
                    return redirect('cart')


def payment_page(request):
    return render(request, 'payment_page.html')

def process_payment(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        card_number = request.POST.get('card_number')
        expiry_date = request.POST.get('expiry_date')
        cvv = request.POST.get('cvv')
        if 'cart' in request.session:
            del request.session['cart']
        request.session['message'] = "Payment successfully completed!"
        return redirect('home')
    else:
        return redirect('home')


def view_session_data(request):
    session_data = request.session
    #request.session.flush()
    return render(request, 'session_data.html', {'session_data': session_data})

