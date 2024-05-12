from typing import OrderedDict

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from chat.notifier import MessageNotifier
from chat.serializers import *
from chat.models import *


class ChatViewSet(ModelViewSet):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer

    def get_queryset(self):
        return self.queryset.filter(participants__in=(self.request.user.id, )).order_by("-id")

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)

        for data in serializer.data:
            participants: list = data['participants']
            for participant in participants:
                if participant['id'] == self.request.user.id:
                    participants.remove(participant)

        return Response(serializer.data)

    @action(detail=True, methods=["GET"])
    def get_messages(self, request, *args, **kwargs):
        queryset = Message.objects.filter(chat_id=kwargs['pk']).order_by("-id")

        serializer = MessageSerializer(queryset, many=True)

        return Response(serializer.data)


class MessageViewSet(ModelViewSet):
    queryset = Message.objects.all().order_by("-id")
    serializer_class = MessageSerializer
    notifier = MessageNotifier()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)
        receiver = Chat.objects.get(id=serializer.data['chat']).participants.exclude(id=self.request.user.id).first()

        self.notifier.notify(receiver.id, serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateMessageSerializer
        return super().get_serializer_class()

