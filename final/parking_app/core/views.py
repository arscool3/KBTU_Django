from django.core.checks import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from .forms import ParkingReservationForm
from .models import DriverLicense, Car, ParkingLot, ParkingSpace, Payment
from .serializers import DriverLicenseSerializer, CarSerializer, ParkingLotSerializer, ParkingSpaceSerializer, PaymentSerializer
from django.utils import timezone
from .tasks import print_invoice
from .utils import calculate_amount

from django.shortcuts import render
from django.contrib.auth.decorators import login_required



class DriverLicenseViewSet(viewsets.ModelViewSet):
    queryset = DriverLicense.objects.all()
    serializer_class = DriverLicenseSerializer

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class ParkingLotViewSet(viewsets.ModelViewSet):
    queryset = ParkingLot.objects.all()
    serializer_class = ParkingLotSerializer

class ParkingSpaceViewSet(viewsets.ModelViewSet):
    queryset = ParkingSpace.objects.all()
    serializer_class = ParkingSpaceSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    @action(detail=False, methods=['get'])
    def overdue_payments(self, request):
        """
        Возвращает список просроченных платежей
        """
        overdue_payments = self.queryset.filter(end_time__lt=timezone.now())
        serializer = self.get_serializer(overdue_payments, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def mark_as_paid(self, request, pk=None):
        """
        Отмечает платеж как оплаченный
        """
        payment = self.get_object()
        payment.is_paid = True
        payment.save()
        return Response({'status': 'Payment marked as paid'})

    def process_parking_payment(request):
        # Ваш код для обработки платежа и генерации данных чека
        invoice_data = {...}

        # Вызов фоновой задачи для отправки чека на почту
        send_invoice_email.send(email="recipient@example.com", invoice_data=invoice_data)

        # Возвращение ответа пользователю или редирект на другую страницу
        return HttpResponse("Чек отправлен на почту")


def parking_lot_detail(request, parking_lot_id):
    parking_lot = ParkingLot.objects.get(pk=parking_lot_id)
    context = {
        'parking_lot': parking_lot,
    }
    return render(request, 'parking_lot_detail.html', context)

def reserve_parking_space(request, parking_lot_id, space_id):
    space = ParkingSpace.objects.get(pk=space_id)
    if request.method == 'POST':
        form = ParkingReservationForm(request.POST)
        if form.is_valid():
            start_time = form.cleaned_data['start_time']
            end_time = form.cleaned_data['end_time']
            amount = calculate_amount(start_time, end_time)
            payment = Payment.objects.create(car=request.user.car, parking_space=space, start_time=start_time, end_time=end_time, amount=amount)
            space.is_occupied = True
            space.save()
            return redirect('parking_lot_detail', parking_lot_id=parking_lot_id)
    else:
        form = ParkingReservationForm()
    return render(request, 'reserve_parking_space.html', {'form': form})


@login_required
def user_profile(request):
    user = request.user
    cars = user.car_set.all()
    payments = user.payment_set.all()

    return render(request, 'user_profile.html', {'user': user, 'cars': cars, 'payments': payments})

def reservation_view(request):
    parking_lots = ParkingLot.objects.all()
    parking_spaces = ParkingSpace.objects.filter(is_occupied=False)
    return render(request, 'reserve.html', {'parking_lots': parking_lots, 'parking_spaces': parking_spaces})

# не доделал
def reserve(request):
    if request.method == 'POST':
        form = ParkingReservationForm(request.POST)
        if form.is_valid():
            parking_space_id = form.cleaned_data['parking_space']
            parking_space = ParkingSpace.objects.get(pk=parking_space_id)
            if parking_space.is_occupied:
                messages.error(request, 'This parking space is already occupied. Please choose another one.')
                return redirect('reserve')
            else:
                start_time = form.cleaned_data['start_time']
                end_time = form.cleaned_data['end_time']
                amount = calculate_amount(start_time, end_time)
                parking_space.is_occupied = True
                parking_space.save()
                form.save()
                messages.success(request, 'Parking space reserved successfully!')
                messages.info(request, f'Amount to pay: {amount} KZT')
                return redirect('home')
    else:
        form = ParkingReservationForm()
    return render(request, 'reserve.html', {'form': form})

def process_parking_payment(request):
    if request.method == 'POST':
        invoice_data = {...}
        print_invoice.send(user=request.user, invoice_data=invoice_data)
        return HttpResponse("Чек сгенерирован и отправлен на печать")
    else:
        return HttpResponse("Метод запроса не поддерживается")