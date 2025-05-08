from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Message
from .serializers import MessageSerializer

class MessageListCreateView(generics.ListCreateAPIView):
    serializer_class = MessageSerializer

    def get_queryset(self):
        user_id = self.request.user.id
        return Message.objects.filter(sender_id=user_id) | Message.objects.filter(receiver_id=user_id)

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)
