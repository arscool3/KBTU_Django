import smtplib
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers
from api.models import *
import random
import string
from src import settings


def send_email(to_email, msg):
    EMAIL_HOST = settings.EMAIL_HOST
    EMAIL_PORT = settings.EMAIL_PORT
    EMAIL_HOST_USER = settings.EMAIL_HOST_USER  # SHED_team@gmail.com
    EMAIL_HOST_PASSWORD = settings.EMAIL_HOST_PASSWORD

    smtp_server = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
    smtp_server.starttls()
    smtp_server.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)

    from_email = EMAIL_HOST_USER
    smtp_server.sendmail(from_email, to_email, msg)


class OrganizationSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)


class RoleSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)


class GroupSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=False, required=False)

    class Meta:
        model = Group
        fields = '__all__'

    def create(self, validated_data):
        instance = Group.objects.create(**validated_data)
        return instance

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name')
        instance.organization = validated_data.get('organization')
        instance.save()
        return instance


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=False)
    username = serializers.CharField(required=False)

    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        print(validated_data)
        instance = self.Meta.model(**validated_data)
        instance.generate_username(instance.name, instance.surname)
        if password is not None:
            instance.set_password(password)

        message = "You were registered to platform SHED!\n" \
                  f"Your username: {instance.username}\n" \
                  f"Your password: {password}"
        subject = "SHED_Registration"
        msg = f'Subject: {subject}\n\n{message}'
        send_email(instance.email, msg)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name')
        instance.surname = validated_data.get('surname')
        instance.username = validated_data.get('username')
        instance.email = validated_data.get('email')
        instance.role = validated_data.get('role')
        instance.group = validated_data.get('group')
        instance.organization = validated_data.get('organization')
        password = validated_data.pop('password')
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class RoomSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=False, required=False)

    class Meta:
        model = Room
        fields = '__all__'

    def create(self, validated_data):
        user = Room.objects.create(**validated_data)
        return user

    def update(self, instance, validated_data):
        instance.room_number = validated_data.get('room_number')
        instance.capacity = validated_data.get('capacity')
        instance.organization = validated_data.get('organization')
        instance.save()
        return instance


class EventsSerializer(serializers.ModelSerializer):
    tutor = UserSerializer(read_only=True)
    room = RoomSerializer(read_only=True)
    group = GroupSerializer(read_only=True)

    tutor_id = serializers.IntegerField(write_only=True)
    room_id = serializers.IntegerField(write_only=True)
    group_id = serializers.IntegerField(write_only=True)
    id = serializers.IntegerField(required=False)

    def validate(self, data):
        if Events.objects.exclude(id=data.get('id', 0)). \
                filter(event_start_time=data.get('event_start_time'),
                       day=data.get('day'),
                       group__id=data.get('group_id')).exists():
            raise serializers.ValidationError({"error": "time is not free"})
        if 9 > data.get('event_start_time') or data.get('event_start_time') > 20:
            raise serializers.ValidationError({"error": "not correct time"})
        return data

    class Meta:
        model = Events
        fields = '__all__'
        depth = 1

    def create(self, validated_data):
        print(validated_data)
        tutor_data = validated_data.pop('tutor_id')
        try:
            tutor = User.objects.get(id=tutor_data)
        except ObjectDoesNotExist:
            raise serializers.ValidationError({'error': 'tutor does not exists'})
        validated_data['tutor'] = tutor

        room_id = validated_data.pop('room_id')
        try:
            room = Room.objects.get(id=room_id)
        except ObjectDoesNotExist:
            raise serializers.ValidationError({'error': 'room does not exists'})
        validated_data['room'] = room

        group_id = validated_data.pop('group_id')
        try:
            group = Group.objects.get(id=group_id)
        except ObjectDoesNotExist:
            raise serializers.ValidationError({'error': 'group does not exists'})
        validated_data['group'] = group

        event = Events.objects.create(**validated_data)
        return event

    def update(self, instance, validated_data):
        instance.discipline = validated_data.get('discipline')
        instance.event_start_time = validated_data.get('event_start_time')
        instance.day = validated_data.get('day')

        room_id = validated_data.pop('room_id')
        try:
            room = Room.objects.get(id=room_id)
        except ObjectDoesNotExist:
            raise serializers.ValidationError({'error': 'room does not exists'})
        instance.room = room

        tutor_data = validated_data.pop('tutor_id')
        try:
            tutor = User.objects.get(id=tutor_data)
        except ObjectDoesNotExist:
            raise serializers.ValidationError({'error': 'tutor does not exists'})
        instance.tutor = tutor

        group_id = validated_data.pop('group_id')
        try:
            group = Group.objects.get(id=group_id)
        except ObjectDoesNotExist:
            raise serializers.ValidationError({'error': 'group does not exists'})
        instance.group = group
        instance.save()
        return instance
