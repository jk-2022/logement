from rest_framework import serializers
from .models import Message
from users.serializers import UserSerializer
from locations.serializers import LogementSerializer

class MessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only=True)
    receiver = UserSerializer(read_only=True)
    logement = LogementSerializer(read_only=True)

    class Meta:
        model = Message
        fields = ['id', 'sender', 'receiver', 'logement', 'content', 'timestamp', 'is_read']
