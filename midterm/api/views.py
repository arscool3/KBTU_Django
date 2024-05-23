import datetime
import json

import jwt
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import *


def get_org_id(request):
    token = request.META.get('HTTP_AUTHORIZATION')
    if token is None:
        raise AuthenticationFailed
    token = token.split()[1]
    decoded_data = jwt.decode(jwt=token,
                              key=settings.SECRET_KEY,
                              algorithms=["HS256"])
    return decoded_data['org_id']


@csrf_exempt
def change_event_status(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    event_id = body['event']
    try:
        instance = Events.objects.get(id=event_id)
    except ObjectDoesNotExist:
        return JsonResponse({'error': "event does not exists"}, safe=False)
    event = instance
    group_id = event.group.id
    users = User.objects.all()
    if event.status:
        event.status = False
        for user in users:
            if user.group is not None and user.group.id == group_id:
                message = f"Your lesson at {event.event_start_time} in {event.room.name} room was canceled!\n"
                subject = f'{event.discipline} at {event.event_start_time}'
                msg = f'Subject: {subject}\n\n{message}'
                send_email(user.email, msg)
    else:
        event.status = True
        for user in users:
            if user.group is not None and user.group.id == group_id:
                message = f"Your lesson at {event.event_start_time} in {event.room.name} room is activate!\n"
                subject = f'{event.discipline} at {event.event_start_time}'
                msg = f'Subject: {subject}\n\n{message}'
                send_email(user.email, msg)

    event = EventsSerializer(event).data
    event['room_id'] = event['room']['id']
    event['tutor_id'] = event['tutor']['id']
    event['group_id'] = event['group']['id']
    serializer = EventsSerializer(instance=instance, data=event)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, safe=False)
    else:
        return JsonResponse(serializer.errors, safe=False)


def get_tutor_events(request, user_id):
    events = []
    for i in range(1, 7):
        for j in range(8, 21):
            if Events.objects.filter(event_start_time=j, day=i, tutor__id=user_id).exists():
                my_object = Events.objects.get(event_start_time=j, day=i, tutor__id=user_id)
                my_object = EventsSerializer(my_object).data
                events.append(my_object)

    return JsonResponse(events, safe=False)


def get_users_events(request, user_id):
    try:
        user = User.objects.get(id=user_id)
    except ObjectDoesNotExist:
        return JsonResponse({'error': 'user does not exist'}, safe=False)
    if user.group is None:
        return JsonResponse({'error': 'user does not contain in group'}, safe=False)
    group_id = user.group.id
    org_id = user.organization.id
    events = []
    for i in range(1, 7):
        for j in range(8, 21):
            if Events.objects.filter(event_start_time=j, day=i, group__id=group_id,
                                     group__organization__id=org_id).exists():
                my_object = Events.objects.get(event_start_time=j, day=i, group__id=group_id,
                                               group__organization__id=org_id)
                my_object = EventsSerializer(my_object).data
                events.append(my_object)
    return JsonResponse(events, safe=False)


def get_available_rooms(request):
    try:
        org_id = get_org_id(request)
    except AuthenticationFailed:
        return JsonResponse({'error': 'not authenticated'})
    time = request.GET.get('hour', None)
    day = request.GET.get('day', None)
    events = Events.objects.filter(event_start_time=time, day=day,
                                   room__organization__id=org_id)
    not_aviable_rooms = []
    if len(events) != 0:
        for event in events:
            not_aviable_rooms.append(event.room.id)
    available_rooms = Room.objects.exclude(id__in=not_aviable_rooms).filter(organization__id=org_id)
    serializer = RoomSerializer(available_rooms, many=True)
    return JsonResponse(serializer.data, safe=False)


class LoginView(APIView):
    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        user = User.objects.get(username=username)
        if user is None:
            raise AuthenticationFailed('user not found')

        if not user.check_password(password):
            raise AuthenticationFailed('incorrect password')

        payload = {
            'user_id': user.id,
            'username': user.username,
            'role': user.role.name,
            'org_id': user.organization.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        }
        token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256').decode('utf-8')
        return Response({
            'user_id': user.id,
            'role': user.role.name,
            'org_id': user.organization.id,
            'token': token
        })


class GroupListAPIView(APIView):
    def get(self, request):
        groups = Group.objects.all()
        serializer = GroupSerializer(groups, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = GroupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GroupDetailAPIView(APIView):
    def get_object(self, group_id):
        try:
            return Group.objects.get(pk=group_id)
        except ObjectDoesNotExist:
            return Response({'error': 'does not exist'}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, group_id):
        instance = self.get_object(group_id)
        if type(instance) == Response:
            return instance
        serializer = GroupSerializer(instance)
        return Response(serializer.data)

    def put(self, request, group_id):
        instance = self.get_object(group_id)
        if type(instance) == Response:
            return instance
        serializer = GroupSerializer(instance=instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, group_id):
        instance = self.get_object(group_id)
        if type(instance) == Response:
            return instance
        instance.delete()
        return Response({'deleted': True})


class UserListAPIView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TutorListAPIView(APIView):
    def get(self, request):
        users = User.objects.all().filter(role=3)
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


class StudentListAPIView(APIView):

    def get(self, request):
        users = User.objects.all().filter(role=2)
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


class UserDetailAPIView(APIView):
    def get_object(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except ObjectDoesNotExist:
            return Response({'error': 'does not exist'}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, user_id):
        instance = self.get_object(user_id)
        if type(instance) == Response:
            return instance
        serializer = UserSerializer(instance)
        return Response(serializer.data)

    def put(self, request, user_id):
        instance = self.get_object(user_id)
        if type(instance) == Response:
            return instance
        serializer = UserSerializer(instance=instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, user_id):
        instance = self.get_object(user_id)
        if type(instance) == Response:
            return instance
        instance.delete()
        return Response({'deleted': True})


class RoomListAPIView(APIView):

    def get(self, request):
        rooms = Room.objects.all()
        serializer = RoomSerializer(rooms, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RoomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RoomDetailAPIView(APIView):
    def get_object(self, room_id):
        try:
            return Room.objects.get(pk=room_id)
        except ObjectDoesNotExist as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, room_id):
        instance = self.get_object(room_id)
        if type(instance) == Response:
            return instance
        serializer = RoomSerializer(instance)
        return Response(serializer.data)

    def put(self, request, room_id):
        instance = self.get_object(room_id)
        if type(instance) == Response:
            return instance
        serializer = RoomSerializer(instance=instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, room_id):
        instance = self.get_object(room_id)
        if type(instance) == Response:
            return instance
        instance.delete()
        return Response({'deleted': True})


class EventListAPIView(APIView):
    def get(self, request):
        categories = Events.objects.all()
        serializer = EventsSerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EventsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EventDetailAPIView(APIView):
    def get_object(self, event_id):
        try:
            return Events.objects.get(pk=event_id)
        except Events.DoesNotExist as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, event_id):
        instance = self.get_object(event_id)
        if type(instance) == Response:
            return instance
        serializer = EventsSerializer(instance)
        return Response(serializer.data)

    def put(self, request, event_id):
        instance = self.get_object(event_id)
        if type(instance) == Response:
            return instance
        serializer = EventsSerializer(instance=instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, event_id):
        instance = self.get_object(event_id)
        if type(instance) == Response:
            return instance
        instance.delete()
        return Response({'deleted': True})
