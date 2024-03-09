import json

from django.contrib.auth import get_user_model
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators import csrf
from django.views.decorators.csrf import csrf_exempt

from .forms import ChatRoomForm
from .models import *


# Create your views here.
def test(request):
    if request.method == 'GET':
        return HttpResponse('test')

def chatPage(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            context = {}
            return render(request, "Page.html", context)
        return redirect("login-user")

@csrf_exempt
def save_message(request):
    if request.method == 'POST':
        data = json.loads(request.body)['data']
        username = data['username']
        message_content = data['message']
        time = data['time']
        user = User.objects.get(username=username)
        message = Message(sender=user, content=message_content, time=time)
        message.save()
        response_data = {
            'status': 'Message saved successfully'
        }
        return JsonResponse(response_data)
    else:
        response_data = {
            'error': 'Only POST method is allowed'
        }
        return JsonResponse(response_data, status=405)

@csrf_exempt
def get_message(request):
    if request.method == 'GET':
        messages = Message.objects.all().values('sender__username', 'content', 'timestamp', 'time')
        messages_list = list(messages)
        return JsonResponse(messages_list, safe=False)
    else:
        response_data = {
            'error': 'Only GET method is allowed'
        }
        return JsonResponse(response_data, status=405)

@csrf_exempt
def create_room(request):
    if request.method == 'POST':
        form = ChatRoomForm(request.POST)
        if form.is_valid():
            room = form.save()
            return JsonResponse({
                'status': 'Created successfully'
            })
    else:
        form = ChatRoomForm()
    return render(request, 'create_room.html', {'form': form})

@csrf_exempt
def get_groups(request):
    if request.method == 'GET':
        chat_rooms = ChatRoom.objects.all().values('id', 'name')
        return JsonResponse(list(chat_rooms), safe=False)


@csrf_exempt
def get_the_group(request, room_name):
    if request.method == 'GET':
        try:
            chat_room = ChatRoom.objects.get(name=room_name)
            messages = chat_room.get_all_messages()
            print(list(messages))
        except ChatRoom.DoesNotExist:
            messages = []

        return render(request, 'room.html', {'room_name': room_name, 'messages': messages})


@csrf_exempt
def save_message_by_room(request, room_name):
    if request.method == 'POST':
        try:

            data = json.loads(request.body)['data']
            username = data['username']
            message_content = data['message']
            time = data['time']
            user = User.objects.get(username=username)
            # Get the ChatRoom object
            chat_room = ChatRoom.objects.get(name=room_name)

            # Create and save the Message
            message = Message(sender=user, content=message_content, time=time)
            message.save()
            chat_room.messages.add(message)
            chat_room.save()
            # Optionally, you can send a response
            response_data = {
                'status': 'success',
                'message': 'Message saved successfully.'
            }
            return JsonResponse(response_data)

        except ChatRoom.DoesNotExist:
            response_data = {
                'status': 'error',
                'message': 'Chat room does not exist.'
            }
            return JsonResponse(response_data, status=404)

        except Exception as e:
            response_data = {
                'status': 'error',
                'message': 'An error occurred while saving the message.'
            }
            return JsonResponse(response_data, status=500)

    else:
        response_data = {
            'status': 'error',
            'message': 'Invalid request method. Only POST requests are allowed.'
        }
        return JsonResponse(response_data, status=405)