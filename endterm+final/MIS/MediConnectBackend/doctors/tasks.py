import dramatiq
from django.utils import timezone

@dramatiq.actor
def send_reminder_email(appointment_id):
    from .models import Appointment
    from django.core.mail import send_mail

    try:
        appointment = Appointment.objects.get(pk=appointment_id)
        send_mail(
            'Appointment Reminder',
            f'Reminder: You have an appointment with {appointment.doctor.profile.first_name} {appointment.doctor.profile.last_name} on {appointment.date_and_time}.',
            'from@mediconnect.com',
            [appointment.patient.profile.email],
            fail_silently=False,
        )
    except Appointment.DoesNotExist:
        pass
