from rest_framework.decorators import api_view
from rest_framework.response import Response
# noinspection PyUnresolvedReferences
from api.models import List
from django.contrib.auth import get_user_model


@api_view(['GET'])
def statistics_detail(request):
    currently_reading_number = List.objects.all().count()
    already_read_number = List.objects.all().count()
    willing_read_number = List.objects.all().count()

    data = {
        'currentlyNumber': currently_reading_number,
        'alreadyNumber': already_read_number,
        'willingNumber': willing_read_number,
    }
    return Response(data)