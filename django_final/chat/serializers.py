from rest_framework import serializers
from chat.models import *
from users.serializers import GetUserInfoSerializer


class ChatSerializer(serializers.ModelSerializer):
    participants = GetUserInfoSerializer(many=True)

    class Meta:
        model = Chat
        fields = "__all__"


class MessageSerializer(serializers.ModelSerializer):
    sender = GetUserInfoSerializer()

    class Meta:
        model = Message
        fields = "__all__"
        read_only_fields = ('sender', )


class CreateMessageSerializer(serializers.ModelSerializer):
    sender = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Message
        fields = "__all__"

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['sender'] = GetUserInfoSerializer(instance.sender).data
        return data
