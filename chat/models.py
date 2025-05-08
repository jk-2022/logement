from django.db import models
from users.models import User
from locations.models import Logement

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    logement = models.ForeignKey(Logement, on_delete=models.CASCADE, related_name='messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"De {self.sender} à {self.receiver} | {self.timestamp.strftime('%d-%m-%Y %H:%M')}"
